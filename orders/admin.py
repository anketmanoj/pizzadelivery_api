from django.contrib import admin
from .models import Orders

# Register your models here.


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('size', 'customer', 'order_status',
                    'quantity', )
    list_filter = ('size', 'order_status', )
    search_fields = ('customer',)
