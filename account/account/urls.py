from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('superman/', admin.site.urls,name='admin'),
    path('', views.index, name='home'),
    path('log/', views.user_login, name='login'),
    path('sign/', views.signup, name='sign_up'),
    path('logout/',views.log_out,name=('logout')),
    path('vip/', include('members.urls',namespace='members')),
    path('products/', include('product.urls',namespace='product')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
