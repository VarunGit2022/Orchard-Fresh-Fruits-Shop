from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from  .models import*
from django.db.models import Q
from django.http import JsonResponse


# Create your views here.

# def move_to_cart(request, saved_item_id):
#     # Get the saved item to move to the cart
#     saved_item = get_object_or_404(SavedItem, id=saved_item_id)

#     # Create a new cart item with the product and quantity from the saved item
#     cart_item = Cart.objects.create(
#         product=saved_item.product,
#         cart=request.user.cart,
#         quantity=saved_item.quantity
#     )

#     # Delete the saved item from the "save for later" list
#     saved_item.delete()

#     messages.success(request, f"{cart_item.product.name} has been moved to your cart.", {'moved_item':cart_item})

#     return redirect('cart')



def home(request):
    fruits = Fruit.objects.all()
    return render(request,'home.html',{'fruits':fruits})

def about(request):
    return render(request,'about.html')

def fruit(request):
    fruits = Fruit.objects.all()
    return render(request,'fruit.html',{'fruits':fruits})

def contact(request):
    if request.method=='POST':
        nm  =request.POST['cname']
        em = request.POST['cemail']
        mn = request.POST['cmobno']
        msg = request.POST['cmessage']
        Contact.objects.create(full_name=nm,email=em,mob_no=mn,message=msg).save()
        messages.success(request,"Your message is Succesfully send!!!")
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')

def testimonial(request):
    return render(request,'testimonial.html')


def user_signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,"congratulations!! Your account is succesfully created")
            fm.save()
    else:
        fm = SignupForm()
    return render(request,'signup.html',{'form':fm})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass =  fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return redirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return redirect('/')

def user_logout(request):
    logout(request)
    return redirect('/')


def detail(request):
    fd = Fruit.objects.get(id=id)
    if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(fruits=fd.id) & Q(user=request.user)).exists()
        print(item_already_in_cart)
    else:
        return redirect('/login/')
    d = {'detail': fd, 'item_already_in_cart': item_already_in_cart}
    return render(request, 'detail.html', d)


def add_cart(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.GET.get('pid')
        product = Fruit.objects.get(id=product_id)
        Cart(user=user,fruits=product).save()

        return redirect('/showcart/')

    return redirect('/login/')

# def move_to_cart(request):
#     if request.user.is_authenticated:
#         user = request.user
#         product_id = request.GET.get('pid')
#         product = Fruit.objects.get(id=product_id)
#         Cart(user=user,fruits=product).save()

#         return redirect('/showcart/')

#     return redirect('/login/')


def view_booking(request):
    if request.user.is_authenticated:
        data = Booking.objects.filter(user=request.user)
        return render(request,'view_booking.html',{'data':data})
    
    return redirect('/login/')


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        #print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = p.quantity* int(p.fruits.price_per_kg)
                amount += (tempamount)
                totalamount = amount+shipping_amount

            return render(request,'cart.html',{'carts':cart , 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request,'emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        c = Cart.objects.get(Q(fruits=pid) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * int(p.fruits.price_per_kg))
            amount += int(tempamount)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)


def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        add = Customer.objects.filter(user=user)
        if add:
            cart_items = Cart.objects.filter(user=user)
            amount = 0
            shipping_amount = 70
            cart_product = [p for p in Cart.objects.all() if p.user == request.user]
            if cart_product:
                for p in cart_product:
                    tempamount = (p.quantity * int(p.fruits.price_per_kg))
                    amount += int(tempamount)
                totalamount  = amount+shipping_amount
                return render(request,'checkout.html',{'totalamount':totalamount,'carts':cart_items,'add':add})
        else:
            return redirect('/profile/')
    return redirect('/login/')


def minus_cart(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        c = Cart.objects.get(Q(fruits=pid) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * int(p.fruits.price_per_kg))
            amount += int(tempamount)
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        pid = request.GET['pid']
        c = Cart.objects.get(Q(fruits=pid) & Q(user=request.user))
        c.delete()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * int(p.fruits.price_per_kg))
            amount += int(tempamount)
        data = {
            'amount': amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)

def address(request):
    user= request.user
    add = Customer.objects.filter(user=user)
    return render(request,'address.html',{'add':add,'active':'btn-primary'} )

def profile(request):
    if request.method == 'POST':
        user = request.user
        messages.success(request,'Your Address is Succesfully Added')
        return render(request,'profile.html',{'active':'btn-primary'}, {'users':user})

    return render(request,'profile.html')

# def booking(request):
#     user = request.user
#     bookid = request.GET.get('bookid')
#     print(bookid)
#     customer = Customer.objects.get(id=bookid)
#     print(customer)
#     cart = Cart.objects.filter(user=user)
#     for  c in cart:
#         Booking(user=user,customer=customer,product=c.fruits,quantity=c.quantity).save()

#         c.delete()
#     return redirect('/viewbooking/')


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Fruit.objects.filter(Q(name__icontains=srch))
            if match:
                nm = Fruit.objects.get(match.name)
                return render(request, 'search.html', {'sr': match}, {'nm': nm})
        else:
            return redirect('/')
    return render(request,'home.html') 

# def save_for_later(request):
#     if request.method == 'GET':
#         user = request.user
#         product_id = request.GET.get('pid')
#         fruit = get_object_or_404(Fruit, id=product_id)
        
#         # Create a new SavedProduct object with the selected fruit and the current user
#         SavedItem.objects.create(fruit=fruit, user=request.user)
#         items = SavedItem.objects.filter(user=user, fruit=fruit)
#         # Return a success response
#         return render(request, 'cart.html', {'saveditems': items})
#     else:
#         # Return a bad request error for requests that are not GET.
#         return JsonResponse({'error': 'Bad request.'}, status=400)
