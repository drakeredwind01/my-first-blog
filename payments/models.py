from django.db import models
from django.contrib.auth.models import User


class Email(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Mom, Jake")
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(help_text="Price in cents (e.g. 2000 = $20.00)")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    notification_recipients = models.ManyToManyField(Email, blank=True)
    notification_subject = models.CharField(max_length=200, default="New sale!")
    notification_message = models.TextField(
        blank=True,
        help_text="Placeholders: {buyer}, {product}, {quantity}, {address}"
    )

    def __str__(self):
        return self.name

    @property
    def price_display(self):
        return f"${self.price / 100:.2f}"


class Order(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_PAID = 'paid'
    STATUS_SHIPPED = 'shipped'
    STATUS_FAILED = 'failed'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_PAID, 'Paid'),
        (STATUS_SHIPPED, 'Shipped'),
        (STATUS_FAILED, 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    stripe_session_id = models.CharField(max_length=200, blank=True)
    stripe_payment_intent = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    shipping_address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} — {self.get_status_display()}"

    @property
    def total(self):
        return sum(item.subtotal for item in self.items.all())

    @property
    def total_display(self):
        return f"${self.total / 100:.2f}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price_at_purchase = models.PositiveIntegerField(help_text="Price in cents at time of purchase")

    def __str__(self):
        return f"{self.quantity}× {self.product.name}"

    @property
    def subtotal(self):
        return self.quantity * self.price_at_purchase

    @property
    def subtotal_display(self):
        return f"${self.subtotal / 100:.2f}"
