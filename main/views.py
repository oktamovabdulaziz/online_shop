from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get("page")
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


def index_view(request):
    user = request.user
    card = []
    total = 0
    if not user.is_anonymous:
        card = Cart.objects.filter(user=user)
    for i in card:
        total += i.product.price
    context = {
        "total": total,
        "card": card,
        "slider": Product.objects.filter(in_slider=True).order_by("-id")[:3],
        "service": Services.objects.all()[:4],
        "product": Product.objects.filter(is_top=True).order_by("-id")[:12],
        "add": Add.objects.all()[:2],
        "blog": Blog.objects.all()[:3],
        "the_bread": Thebread.objects.last(),
        "many_logo": Many_logo.objects.all(),
        "info": Information.objects.last(),
        "health": Health.objects.last(),
        "is_new": Product.objects.filter(is_new=True)[:5]
    }
    return render(request, 'index.html', context)


def about_view(request):
    context = {
        "info": Information.objects.last(),
        "many_logo": Many_logo.objects.all(),
        "about": About.objects.last(),
        "video": Video.objects.last(),
        "beard": Beard.objects.last(),
    }
    return render(request, "about.html", context)


def blog_view(request):
    blogs = Blog.objects.all()
    context = {
            "info": Information.objects.last(),
            "blog": Blog.objects.all(),
            "blogs": PagenatorPage(blogs, 3, request),
            "is_new": Blog.objects.filter(is_new=True)
    }
    return render(request, "blog.html", context)


def blog_detail_view(request, pk):
    user = request.user
    card = []
    total = 0
    blog = Blog.objects.get(id=pk)
    if not user.is_anonymous:
        card = Cart.objects.filter(user=user)
    for i in card:
        total += i.product.price
    context = {
        "total": total,
        "card": card,
        "info": Information.objects.last(),
        "blog": blog,
    }
    return render(request, "blog-details.html", context)


def contact_view(request):
    context = {
        "info": Information.objects.last(),
    }
    return render(request, "contact.html", context)


def add_contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
        )
    return redirect("contact")


def faq_view(request):
    context = {
        "info": Information.objects.last(),
    }
    return render(request, "faq.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Login yoki parol xato!")
            return redirect("login")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def page_404_view(request):
    return render(request, "page-not-found.html")


def shop_view(request):
    products = Product.objects.all()
    user = request.user
    card = []
    total = 0
    if not user.is_anonymous:
        card = Cart.objects.filter(user=user)
    for i in card:
        total += i.product.price
    context = {
        "products": PagenatorPage(products, 1, request),
        "total": total,
        "card": card,
        "category": Category.objects.all(),
        "info": Information.objects.last(),
    }
    return render(request, "shop.html", context)


def cart_view(request):
    user = request.user
    card = []
    total = 0
    if not user.is_anonymous:
        card = Cart.objects.filter(user=user)
    for i in card:
        total += i.product.price
    context = {
       "total": total,
       "card": card,
       "info": Information.objects.last(),

    }
    return render(request, "shop-cart.html", context)


def checkout_view(request):
    user = request.user
    card = []
    total = 0
    if not user.is_anonymous:
        card = Cart.objects.filter(user=user)
    for i in card:
        total += i.product.price
    context = {
        "total": total,
        "card": card,
        "info": Information.objects.last(),
        "region": Region.objects.all(),
    }
    return render(request, "shop-checkout.html", context)


def product_detail_view(request):
    user = request.user
    card = []
    total = 0
    if not user.is_anonymous:
        card = Cart.objects.filter(user=user)
    for i in card:
        total += i.product.price
    context = {
        "total": total,
        "card": card,
        "info": Information.objects.last(),

    }
    return render(request, "shop-single-product.html", context)


def search_view(request):
    q = request.GET.get('q')
    products = []
    if q is not None:
        products = Product.objects.filter(name__icontains=q)
    user = request.user
    card = []
    total = 0
    if not user.is_anonymous:
        card = Cart.objects.filter(user=user)
    for i in card:
        total += i.product.price
    context = {
        "products": products,
        "total": total,
        "category": Category.objects.all(),
        "info": Information.objects.last(),

    }
    return render(request, 'search.html', context)


def category_view(request, pk):
    products = Product.objects.filter(category_id=pk)
    user = request.user
    card = []
    total = 0
    if not user.is_anonymous:
        card = Cart.objects.filter(user=user)
    for i in card:
        total += i.product.price
    context = {
        "products": products,
        "total": total,
        "card": card,
        "category": Category.objects.all(),
        "info": Information.objects.last(),

    }
    return render(request, 'category.html', context)


def wishlist_view(request):
    user = request.user
    card = []
    wishlist = []
    if not user.is_anonymous:
        card = Cart.objects.filter(user=user)
        wishlist = Wishlist.objects.filter(user=user)
    total = 0
    for i in card:
        total += i.product.price
    context = {
        "total": total,
        "wishlist": wishlist,
        "card": card,
        "info": Information.objects.last(),
    }
    return render(request, 'wishlist.html', context)


def add_cart_view(request, pk):
    user = request.user
    if not user.is_anonymous:
        product = Product.objects.get(id=pk)
        if Cart.objects.filter(user=user, product=product).count() == 0:
            Cart.objects.create(
                user=user,
                product=product,
                quantity=1
            )
        return redirect('index')
    else:
        return redirect('login')


def add_wishlist_view(request, pk):
    user = request.user
    if not user.is_anonymous:
        product = Product.objects.get(id=pk)
        if Wishlist.objects.filter(user=user, product=product).count() == 0:
            Wishlist.objects.create(
                user=user,
                product=product,
            )
        return redirect('index')
    else:
        return redirect('login')


def remove_cart_view(request, pk, page):
    Cart.objects.get(id=pk).delete()
    if page == 'index':
        return redirect('index')
    elif page == 'cart':
        return redirect('cart')
    elif page == 'shop':
        return redirect('shop')
    elif page == 'search':
        q = request.GET.get('q')
        return redirect('search?q=q')


def remove_wishlist_view(request, pk):
    Wishlist.objects.get(id=pk).delete()
    return redirect("wishlist")


def clear_cart_view(request):
    user = request.user
    Cart.objects.filter(user=user).delete()
    return redirect("cart")


def create_order_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address = request.POST.get("address")
        apartment = request.POST.get("apartment")
        region = request.POST.get("region")
        postal_code = request.POST.get("postal_code")
        user = request.user
        order = Order.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            address=address,
            apartment=apartment,
            region_id=region,
            postal_code=postal_code,
        )
        for i in Cart.objects.filter(user=user):
            OrderItem.objects.create(
                product=i.product,
                order=order,
                quantity=i.quantity,
                price=i.product.price
            )
        Cart.objects.filter(user=user).delete()
    return redirect("checkout")


def product_detail(request, id):
    product = Product.objects.get(id=id)
    print(product.name)
    context = {
        "product": product,
        "info": Information.objects.last(),
    }
    return render(request, "product-detail.html", context)
