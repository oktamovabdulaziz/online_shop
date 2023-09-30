from django.urls import path
from .views import *


urlpatterns = [
    path('category/list/', category_list),
    path('category/create/', create_category),
    path('category/detail/<int:id>/',  category_detail),
    path('product/list/', product_list),
    path('product/detail/<int:id>/',  product_detail),
    path('region/list/', region_list),
    path('region/detail/<int:id>/', region_detail),
    path('contact/list/', contact_list),
    path('blog/list/', blog_list),
    path('blog/detail/<int:id>/', blog_detail),
    path('thebread/list/', thebread_list),
    path('thebread/detail/<int:id>/', thebread_detail),
    path('information/list/', information_list),
]

