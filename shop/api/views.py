from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from main.models import Product, Category, Region, Contact, Blog, Thebread
from .serializers import (
    CategoryListSerializer,
    CategoryDetailSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    RegionListSerializer,
    RegionDetailSerializer,
    ContactListSerializer,
    BlogListSerializer,
    BlogDetailSerializer,
    ThebreadListSerializer,
    ThebreadDetailSerializer,
)



@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializers_data = CategoryListSerializer(categories, many=True)
    return Response({'data':serializers_data.data})

    


@api_view(['GET'])
def category_detail(request, id):
    categories = get_object_or_404(Category, id=id)
    serializers_data = CategoryDetailSerializer(categories)
    return Response({'data':serializers_data.data})



@api_view(['GET'])
def product_list(request):
    product = Product.objects.all()
    ser_data = ProductListSerializer(product, many=True)
    return Response({"data": ser_data.data})


@api_view(['GET'])
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    ser_data = ProductDetailSerializer(product)
    return Response({"data":ser_data.data})


@api_view(['GET'])
def region_list(request):
    region = Region.objects.all()
    serializer_data = RegionListSerializer(region, many=True)
    return Response({"data": serializer_data.data})


@api_view(['GET'])
def region_detail(request, id):
    region = get_object_or_404(Region, id=id)
    serializer_data = RegionDetailSerializer(region)
    return Response({"data": serializer_data.data})


@api_view(['GET'])
def contact_list(request):
    contact = Contact.objects.all()
    ser_data = ContactListSerializer(contact, many=True)
    return Response({"data": ser_data.data})



@api_view(['GET'])
def blog_list(request):
    blog = Blog.objects.all()
    serializer_data = BlogListSerializer(blog, many=True)
    return Response({'data': serializer_data.data})


@api_view(["GET"])
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    serializer_data = BlogDetailSerializer(blog)
    return Response({"data": serializer_data.data})

@api_view(["GET"])
def thebread_list(request):
    thebread = Thebread.objects.all()
    serializer_data = ThebreadListSerializer(thebread, many=True)
    return Response({"data": serializer_data.data})


@api_view(['GET'])
def thebread_detail(request, id):
    thebread = get_object_or_404(Thebread, id=id)
    serializer_data = ThebreadDetailSerializer(thebread)
    return Response({'data': serializer_data.data})