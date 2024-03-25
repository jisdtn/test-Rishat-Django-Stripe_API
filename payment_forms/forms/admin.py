from django.contrib import admin

from payment_forms.forms.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
