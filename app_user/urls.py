from django.urls import path, include
from .views import *

app_name = 'app_user'

urlpatterns = [
    path('signin/', SigninView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('account/', AccountView.as_view(), name='account'),
    path('signout/', signoutView, name='signout'),
   
]