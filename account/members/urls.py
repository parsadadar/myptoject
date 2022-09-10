from django.urls import path,include
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .forms import LoginForm

app_name = 'members'


urlpatterns = [
    path('profile/', profile, name='users_profile'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='site/login.html', authentication_form=LoginForm), name='login'),
    #path('register/', RegisterView, name='users_register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
