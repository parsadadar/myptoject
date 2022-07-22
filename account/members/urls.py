from django.urls import path
from members import views

urlpatterns = [
    path('', views.halo, name='member_helo'),
    path('log/',views.log, name='member_log'),
    path('logt/', views.logt, name='member_logout'),
    path('user/<int:id>/',views.user, name='member_user'),
    path('adi/',views.adi, name='member_user')
]
