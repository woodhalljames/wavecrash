from django.urls import path
from .views import *

app_name='product'

urlpatterns = [
    path('detail/<slug:slug>', ProductView.as_view(),name="product-page"),
    path('all-category/', AllCategoryView.as_view(),name="all-category"),
    path('men/', MenCategoryView.as_view(), name='men'),
    path('accessories/', AccessoriesCategoryView.as_view(), name='accessories'),
    path('women/', WomenCategoryView.as_view(), name='women'),
    path('pets/', PetsCategoryView.as_view(), name='pets'),
    path('electronics/', ElectronicsCategoryView.as_view(), name='electronics'),
    path('furniture/', FurnitureCategoryView.as_view(), name='furniture'),
    path('search/', SearchCategoryView.as_view(), name='search-category'),
    path('filter/', FilterCategoryView.as_view(), name='filter-category'),
    path('sort/', SortView.as_view(), name='sort-category'),
    path('size-product/', sizeProduct, name='size-product'),
    path('color-product/', colorProduct, name='color-product'),
    path('product/post-review/', postReview, name='post-review'),
    ]