from django.urls import path
from . import views

urlpatterns = [
    path('adm/', views.adm,name='admin_site'),
    path('',views.spec,name='1313'),
    path('produt/',include("produt.urls",namespace='account')),
    path('<int:cod>/', views.special_num),
    path('<str:cod>/', views.special,name='010123'),
]
