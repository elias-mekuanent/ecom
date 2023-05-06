from django.contrib import admin
from .models import Product,Customer,Cart

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','discounted_price','catagory']
@admin.register(Customer)
class CustomerProfileForm(admin.ModelAdmin):
    list_display =['id','user','locality','city','mobile','state','zipcode']
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']