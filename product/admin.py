from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Size)
admin.site.register(Color)

admin.site.register(Discount)
admin.site.register(Offer)
admin.site.register(Deal)
admin.site.register(Rating)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'getGender', 'active', 'onSale')

    


@admin.register(ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ('itemNumber','name', 'product', 'color', 'size', 'price', 'stock')



