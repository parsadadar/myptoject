from django.urls import path,include
from .views import *

app_name= "product"

urlpatterns = [
    path('', index,name='list'),
    path('ebook/', ebook,name='ebook_shop'),
    path('all/',all_book,name="all_books"),
    path('details/<int:id>', details,name='details'),
    path('delete/<int:id>/', delete ),
    path('update/<int:id>', update, name="update"),
    path('delete/noajax/<int:id>', delete_noajax, name="delete_noajax"),
    path('class_templateview_index/', ClassIndex.as_view(), name="class_templateview_list"),
    path('class_view_index/', ClassViewIndex.as_view(), name="class_view_list"),
    path('class_listview_index/', ClassList.as_view(), name="class_listview_list"),
    path('class_details/<int:pk>', ClassDetails.as_view(), name="class_details"),
]
