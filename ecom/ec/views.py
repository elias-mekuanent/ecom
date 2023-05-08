from urllib import request
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from . models import Product,Customer,Cart
from django.db.models import Count
from django.contrib import messages
from . forms import CustomerRegistrationForm,CustomerProfileForm
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")
def contactus(request):
    return render(request,"contactus.html")
class CategoryView(View):
        def get(self,request,val):
            product=Product.objects.filter(catagory=val)
            title = Product.objects.filter(catagory=val).values('title')       
            return render(request, "category.html",locals())

class CategoryTitle(View):
        def get(self,request,val):
            product=Product.objects.filter(title=val)
            title = Product.objects.filter(catagory=product[0].catagory).values('title')       
            return render(request, "category.html",locals())
class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"ProductDetail.html", locals())
class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, "customerregistration.html",locals())
    def post(self,request):
        form=CustomerRegistrationForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request,"congratulations! user register succesfully")
        else:
            messages.warning(request, "invalid input data")
        return render(request, "customerregistration.html",locals())

class ProfileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request,"profile.html", locals())

    def post(self,request):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg= Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"congratulations! user profile added succesfully")
        else:
            messages.warning(request, "invalid input data")
        return render(request,"profile.html", locals())

def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,"address.html",locals())
class update(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,"update.html",locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
          
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.state=form.cleaned_data['state']
            add.mobile=form.cleaned_data['mobile']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"congratulations! you updated user profile successfully!!")
        else:
            messages.warning(request,"Invalid Input!!")
        return redirect("address")

def add_to_cart(request):
    user=  request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user ,product=product).save()
    return redirect("/cart")

def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value = p.quantity*p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request, 'add_to_cart.html',locals())

def plus_cart(request):
    if request.method== 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart   = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity*p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40 
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        #print(prod_id)
        return JsonResponse(data)
    
