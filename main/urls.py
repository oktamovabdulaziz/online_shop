from django.urls import path
from .views import *

urlpatterns = [
    path("", index_view, name="index"),
    path("about/", about_view, name="about"),
    path("blog/", blog_view, name="blog"),
    path("blog_detail/<int:pk>/", blog_detail_view, name="blog_detail"),
    path("contact/", contact_view, name="contact"),
    path("faq/", faq_view, name="faq"),
    path("login/", login_view, name="login"),
    path("page_404/", page_404_view, name="page_404"),
    path("shop/", shop_view, name="shop"),
    path("cart/", cart_view, name="cart"),
    path("checkout/", checkout_view, name="checkout"),
    path("product_detail/", product_detail_view, name="product_detail"),
    path("logout/", logout_view, name="logout"),
    path("add-cart/<int:pk>/", add_cart_view, name="add-cart"),
    path("add-wishlist/<int:pk>/", add_wishlist_view, name="add-wishlist"),
    path("remove-cart/<int:pk>/<str:page>/", remove_cart_view, name="remove-cart"),
    path("search/", search_view, name="search"),
    path("category/<int:pk>/", category_view, name="category"),
    path("wishlist/", wishlist_view, name="wishlist"),
    path("remove-wishlist/<int:pk>/", remove_wishlist_view, name="remove-wishlist"),
    path("add-contact/", add_contact_view, name="add-contact"),
    path("clear-cart/", clear_cart_view, name="clear-cart"),
    path("create-order/", create_order_view, name="create-order"),
    path("product/<int:id>/", product_detail, name="product-detail"),
]















