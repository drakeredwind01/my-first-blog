from django.contrib import admin
from .models import Email, Product, Order, OrderItem


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'email')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('price_at_purchase',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_display', 'stock', 'active')
    list_filter = ('active',)
    search_fields = ('name',)
    filter_horizontal = ('notification_recipients',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_display', 'created_at')
    list_filter = ('status',)
    search_fields = ('stripe_session_id', 'stripe_payment_intent', 'user__username')
    readonly_fields = ('stripe_session_id', 'stripe_payment_intent', 'created_at')
    inlines = [OrderItemInline]
