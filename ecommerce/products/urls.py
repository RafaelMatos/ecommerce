from django.conf.urls import url
from django.urls import path,re_path


from .views import (
    ProductListView,
    # product_list_view,
    # ProductDetailView,
    # product_detail_view,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView,
    ProductDetailSlugView
    )



urlpatterns = [
    path('',ProductListView.as_view()),
    re_path('^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view()),    
    
]


