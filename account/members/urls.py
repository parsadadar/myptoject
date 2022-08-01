from django.urls import path

from . import views

urlpatterns = [
    path('<int:cod>/', views.special_num),
    path('<str:cod>/', views.special,name='010123'),
]
