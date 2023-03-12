from django.db import models
import os
from django.utils.text import slugify
from django.db.models import Avg
from math import floor, ceil, modf
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.

def category_image(instance, filename):
    upload_to = '{}_files/'.format(instance.name)
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}_image.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=category_image)

    def __str__(self):
        return self.name

def subcategory_image(instance, filename):
    upload_to = '{}_files/{}/'.format(instance.category.name,instance.name)
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}_image.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=subcategory_image, null=True, blank=True)

    def __str__(self):
        return str(self.category.name) + ' - ' + str(self.name)


class Color(models.Model):
    name = models.CharField(max_length=100)
    colorCode = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Size(models.Model):
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategorySizes')
    size = models.CharField(max_length=100)

    def __str__(self):
        return str(self.subCategory.name) + ' - ' + str(self.size)

class Discount(models.Model):
    name = models.CharField(max_length=250)
    discount = models.PositiveIntegerField()

    def __str__(self):
        return self.name

def offer_image(instance, filename):
    upload_to = 'Offer_Files/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)

class Offer(models.Model):
    name = models.CharField(max_length=250)
    discount = models.PositiveIntegerField()
    image = models.ImageField(upload_to=offer_image, null=True, blank=True)
    
    def __str__(self):
        return self.name

def deal_image(instance, filename):
    upload_to = 'Deal_Files/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)

class Deal(models.Model):
    name = models.CharField(max_length=250)
    discount = models.PositiveIntegerField()
    image = models.ImageField(upload_to=deal_image, null=True, blank=True)
    
    def __str__(self):
        return self.name

def product_image(instance, filename):
    upload_to = '{}_files/{}/'.format(instance.category.name,instance.subCategory.name)
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)

class Product(models.Model):
    GENDERS = (
        ('M','Male'),
        ('F', 'Female')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoryProducts')
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategoryroducts')
    gender = models.CharField(max_length=1, choices=GENDERS, blank=True, null=True)
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=350, null=True, blank=True, default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature1 = models.CharField(max_length=250, null=True, blank=True, default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature2 = models.CharField(max_length=250, null=True, blank=True, default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature3 = models.CharField(max_length=250, null=True, blank=True, default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature4 = models.CharField(max_length=250, null=True, blank=True, default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    feature5 = models.CharField(max_length=250, null=True, blank=True, default='lorem ipsum lorem ipsum lorem ipsum lorem ipsum')
    onSale = models.BooleanField(default=False)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=product_image)

    def __str__(self):
        return self.name
    
    def getGender(self):
        return self.get_gender_display()

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        product_variations = ProductVariation.objects.filter(product__name=self.name)
        if product_variations.count() > 0:
                for product in product_variations:
                    if product.product.onSale:
                        discount_price = product.get_discount_price()
                        if isinstance(discount_price, float):
                            dec = modf(discount_price)[0]
                            if dec < 0.5:
                                price = floor(discount_price)
                            else:
                                price = ceil(discount_price)
                        else: 
                            price = discount_price
                        product.discountPrice = price
                    else:
                        product.discountPrice = product.price
                    product.save()

def product_variation_image(instance, filename):
    upload_to = '{}_files/{}/{}_variations/'.format(instance.product.category.name,
                                                   instance.product.subCategory.name,
                                                   instance.product.subCategory.name)
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name,ext)
    return os.path.join(upload_to, filename)

class ProductVariation(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productVariations')
    slug = models.CharField(max_length=350, null=True, blank=True)
    itemNumber = models.PositiveIntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)
    image2 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)
    image3 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)
    image4 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)
    image5 = models.ImageField(upload_to=product_variation_image, null=True, blank=True)
    price = models.PositiveIntegerField()
    discountPrice = models.PositiveIntegerField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name
  
    def number(self):   
        count = ProductVariation.objects.count()
        if count == 0:
            return 1
        else:
            last_object = ProductVariation.objects.order_by('-id')[0]
            return last_object.id + 1
    
    def get_discount_price(self):
        product = self.product
        if product.onSale:
            if product.discount:
                percent = product.discount.discount
            elif product.deal:
                percent = product.deal.discount
            elif product.offer:
                percent = product.offer.discount
            else:
                percent = 0
            price_red = (percent/100) * self.price
            price = self.price - price_red
            return price
        else:
            return self.price

    def save(self, *args, **kwargs):
        if not self.itemNumber:
            self.itemNumber = self.number()
        if not self.name:
            self.name = self.product.get_gender_display() + '-' + self.product.name + '-' + self.color.name + '-' + self.size.size
        if not self.slug:
            self.slug = slugify(self.name)
        self.discountPrice = self.get_discount_price()
        super(ProductVariation, self).save(*args, **kwargs)

    def avg_rating(self):
        #check if more than one rating for the product
        rating_count = Rating.objects.filter(product_variation__name=self.name).count()
        if rating_count > 1:
            ratings = Rating.objects.filter(product_variation__name=self.name).aggregate(Avg('rating'))
            ratings = ratings['rating__avg']
        elif rating_count == 1:
            ratings = Rating.objects.get(product_variation__name=self.name).rating
        else:
            ratings = 1

        #check if the number is float or not
        if isinstance(ratings, float):
            dec = modf(ratings)[0]
            if dec < 0.5:
                rating = floor(ratings)
            else:
                rating = ceil(ratings)
        else: 
            rating = ratings
        return rating


class Rating(models.Model):
    product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, related_name='product_ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product_ratings')
    rating = models.SmallIntegerField(default=3)
    review = models.CharField(max_length=80, default='Nice product')

    def __str__(self):
        return str(self.product_variation) + ' - ' + str(self.rating)

