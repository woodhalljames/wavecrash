from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, View
from django.utils.text import slugify
from order.models import *

from .models import *
# Create your views here.


class AllCategoryView(View):
    def get(self, *args, **kwargs):
        products = ProductVariation.objects.all().order_by('-id')
        paginator = Paginator(products, 12) # Show 12 products per page.
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
                 'page_obj':page_obj,
                 'sub_categories': SubCategory.objects.all(),
                 'colors': Color.objects.all(),
                 'sizes': Size.objects.all().values('size').distinct(),
                    }
        return render(self.request, 'product/category-page.html', context)

class MenCategoryView(View):
    def get(self, *args, **kwargs):
        products = ProductVariation.objects.filter(product__gender='M')
        paginator = Paginator(products, 12) # Show 16 products per page.
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'page_obj':page_obj,
            'sub_categories': SubCategory.objects.filter(category__name='Men'),
            'colors': Color.objects.all(),
            'sizes': Size.objects.all().values('size').distinct(),
        }
        return render(self.request, 'product/category-page.html', context)

class AccessoriesCategoryView(View):
    def get(self, *args, **kwargs):
        products = ProductVariation.objects.order_by('-id')
        paginator = Paginator(products, 12) # Show 12 products per page.
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'page_obj':page_obj,
            'sub_categories': SubCategory.objects.filter(category__name='Accessories'),
            'colors': Color.objects.all(),
            'sizes': Size.objects.all().values('size').distinct(),
        }
        return render(self.request, 'product/category-page.html', context)

class ElectronicsCategoryView(View):
    def get(self, *args, **kwargs):
        products = ProductVariation.objects.order_by('-id')
        paginator = Paginator(products, 12) # Show 12 products per page.
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'page_obj':page_obj,
            'sub_categories': SubCategory.objects.filter(category__name='Electronics'),
            'colors': Color.objects.all(),
            'sizes': Size.objects.all().values('size').distinct(),
        }
        return render(self.request, 'product/category-page.html', context)


class WomenCategoryView(View):
    def get(self, *args, **kwargs):
        products = ProductVariation.objects.filter(product__gender='F')
        paginator = Paginator(products, 12) # Show 12 products per page.
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'page_obj':page_obj,
            'sub_categories': SubCategory.objects.filter(category__name='Women'),
            'colors': Color.objects.all(),
            'sizes': Size.objects.all().values('size').distinct(),
        }
        return render(self.request, 'product/category-page.html', context)

class PetsCategoryView(View):
    def get(self, *args, **kwargs):
        products = ProductVariation.objects.order_by('-id')
        paginator = Paginator(products, 12) # Show 16 products per page.
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'page_obj':page_obj,
            'sub_categories': SubCategory.objects.filter(category__name='Pets'),
            'colors': Color.objects.all(),
            'sizes': Size.objects.all().values('size').distinct(),
        }
        return render(self.request, 'product/category-page.html', context)

class FurnitureCategoryView(View):
    def get(self, *args, **kwargs):
        products = ProductVariation.objects.order_by('-id')
        paginator = Paginator(products, 12) # Show 16 products per page.
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'page_obj':page_obj,
            'sub_categories': SubCategory.objects.filter(category__name='Furniture'),
            'colors': Color.objects.all(),
            'sizes': Size.objects.all().values('size').distinct(),
        }
        return render(self.request, 'product/category-page.html', context)

class ProductView(View): 
	def get(self, *args, **kwargs):
		return render(self.requests, 'product/product-page.html')

#add views in site to database
class AddCategory(CreateView):
	model = CategoryView
	fields = ('__all__')
	
