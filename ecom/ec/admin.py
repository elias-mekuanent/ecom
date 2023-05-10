from django.contrib import admin
from .models import Product,Customer,Cart,Payment,OrderPlaced 

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
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','chapa_order_id','chapa_payment_status','chapa_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']