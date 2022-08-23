from django.urls import path,include
from . import views

app_name= "product"

urlpatterns = [
    path('', views.index,name=''),
    path('details/<int:id>', views.details,name='details'),
    path('delete/<int:id>/', views.delete ),
    path('update<int:id>/', views.update,name='010123'),
]
