from django.urls import path
from . import views

app_name= "product"

urlpatterns = [
    path('', views.index,name=''),
    path('details/<int:id>', details,name='details'),
    path('delete/<int:id>/', delete ),
    path('/update<int:id>/', update,name='010123'),
]
