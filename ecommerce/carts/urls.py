from django.conf.urls import url
from django.urls import path,re_path


from .views import (
    cart_home,
    cart_update,
    checkout_home,
    )

app_name = 'carts'


urlpatterns = [
    path('',cart_home, name='home'),
    re_path('update/$',cart_update,name='update'),
    re_path('checkout/$',checkout_home,name='checkout'),    
    
]


