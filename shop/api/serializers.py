from rest_framework import serializers
from main.models import Category, Product, Region, Contact, Blog, Thebread


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductListSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = ["name", "category"]



class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1



class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'



class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class ThebreadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thebread
        fields = '__all__'


class ThebreadDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thebread
        fields = '__all__'
