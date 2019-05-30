from django.shortcuts import render
from .models import Cart

def create_cart(user = None):
    cart_obj = Cart.objects.create(user = None)
    print('New cart created')
    return cart_obj

def cart_home(request):
    # del request.session['cart_id']
    
    cart_id = request.session.get("cart_id",None)
    
    qs = Cart.objects.filter(id = cart_id)
    if qs.count() == 1:
        print('Cart ID exists')
        cart_obj = qs.first()
        if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = Cart.objects.new(user = request.user)
        request.session['cart_id'] = cart_obj.id
        
        
        # cart_obj = Cart.objects.get(id=cart_id)
    # print(request.session)
    # # print(dir(request.session))
    # key = request.session.session_key
    # print("Key:" + key)
    # request.session.set_expiry(300) #5 minutes 
    # 'session_key', 'set_expiry'
    request.session['first_name'] = "Justin"
    return render(request,"cart/home.html",{})