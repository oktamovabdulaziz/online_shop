from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import string
import random


class Region(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="Product/")
    in_slider = models.BooleanField(default=False)
    is_top = models.BooleanField(default=True)
    description = models.CharField(max_length=255)
    is_new = models.BooleanField(default=False)

class Services(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Add(models.Model):
    photo = models.ImageField(upload_to="Add/")


class Thebread(models.Model):
       photo = models.ImageField(upload_to="The_bread/")
       name = models.CharField(max_length=255)
       lastname = models.CharField(max_length=255)
       text = models.TextField()
       browse = models.CharField(max_length=255)


class Blog(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="Blog/")
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=255, unique=True, blank=True)
    is_new = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            if Blog.objects.filter(slug=slugify(self.name)).count() > 0:
                bl = Blog.objects.last()
                self.slug = f"{self.name}{bl.id+1}"
            else:
                self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Many_logo(models.Model):
    logo = models.ImageField(upload_to="Many_logo/")



class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Information(models.Model):
    logo = models.ImageField(upload_to="website_logo/")
    company_name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    tw = models.CharField(max_length=255)
    pin = models.CharField(max_length=255)
    ins = models.CharField(max_length=255)
    fb = models.CharField(max_length=255)
    map = models.CharField(max_length=255)


class Health(models.Model):
    photo = models.ImageField(upload_to="Health/")
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    view = models.CharField(max_length=255)


class About(models.Model):
    photo = models.ImageField(upload_to="About/")
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)


class Beard(models.Model):
    photo = models.ImageField(upload_to="Beard/")
    mission = models.TextField()
    vision = models.TextField()
    goal = models.TextField()

class Video(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='Video/')
    youtube = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="Video/")



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    apartment = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

