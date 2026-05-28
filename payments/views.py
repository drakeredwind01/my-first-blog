from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView
import stripe

from .models import Product, Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(active=True)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        return JsonResponse({'publicKey': settings.STRIPE_PUBLISHABLE_KEY})


@csrf_exempt
def create_checkout_session(request):
    if request.method != 'GET':
        return HttpResponse(status=405)

    product_id = request.GET.get('product_id')
    quantity = int(request.GET.get('quantity', 1))
    product = get_object_or_404(Product, id=product_id, active=True)

    domain = request.build_absolute_uri('/').rstrip('/')

    order = Order.objects.create(
        user=request.user if request.user.is_authenticated else None,
        status=Order.STATUS_PENDING,
    )
    OrderItem.objects.create(
        order=order,
        product=product,
        quantity=quantity,
        price_at_purchase=product.price,
    )

    try:
        session = stripe.checkout.Session.create(
            client_reference_id=order.pk,
            success_url=f"{domain}/payments/success/?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{domain}/payments/cancelled/",
            payment_method_types=['card'],
            mode='payment',
            shipping_address_collection={'allowed_countries': ['US', 'CA']},
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {'name': product.name},
                    },
                    'quantity': quantity,
                }
            ],
        )
        order.stripe_session_id = session.id
        order.save()
        return JsonResponse({'sessionId': session.id})
    except Exception as e:
        order.status = Order.STATUS_FAILED
        order.save()
        return JsonResponse({'error': str(e)}, status=400)


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        _handle_checkout_complete(event['data']['object'])

    return HttpResponse(status=200)


def _handle_checkout_complete(session):
    order_id = session.get('client_reference_id')
    if not order_id:
        return

    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return

    order.stripe_session_id = session['id']
    order.stripe_payment_intent = session.get('payment_intent', '')
    order.status = Order.STATUS_PAID

    shipping = session.get('shipping_details') or session.get('shipping')
    if shipping:
        addr = shipping.get('address', {})
        order.shipping_address = '\n'.join(filter(None, [
            shipping.get('name', ''),
            addr.get('line1', ''),
            addr.get('line2', ''),
            f"{addr.get('city', '')}, {addr.get('state', '')} {addr.get('postal_code', '')}".strip(', '),
            addr.get('country', ''),
        ]))

    order.save()
    _send_notifications(order)


def _send_notifications(order):
    for item in order.items.select_related('product').all():
        product = item.product
        recipients = list(
            product.notification_recipients.filter(active=True).values_list('email', flat=True)
        )
        if not recipients:
            continue
        message = product.notification_message.format(
            buyer=order.user.username if order.user else 'Guest',
            product=product.name,
            quantity=item.quantity,
            address=order.shipping_address or 'Not provided',
        )
        send_mail(
            subject=product.notification_subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipients,
            fail_silently=True,
        )
