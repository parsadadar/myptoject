from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('log/', views.user_login, name='login'),
    path("sign/", views.signup, name='sign_up'),
    path('vip/', include('members.urls',namespace='members')),
    path('products/', include('product.urls',namespace='product')),
]
