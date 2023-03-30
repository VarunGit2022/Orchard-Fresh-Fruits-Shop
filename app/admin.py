from django.contrib import admin
from .models import*
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.
@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ['id','name','price_per_kg','image']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user','fruits','quantity']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'user', 'mobile_no','gender','mobile_no','email']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user','customer','product','ordered_date','customer_info','status','quantity']

    def customer_info(self,obj):
        link = reverse("admin:app_customer_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','mob_no','message']

@admin.register(SavedItem)
class SavedItemAdmin(admin.ModelAdmin):
    list_display = ['product','quantity']