from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import UserRegisterView, UserProfileView, pass_verification, restore_password

app_name = UsersConfig.name

urlpatterns = [
    path('', never_cache(LoginView.as_view(template_name='users/login.html')), name='login'),
    path('logout/', never_cache(LogoutView.as_view()), name='logout'),
    path('register/', never_cache(UserRegisterView.as_view()), name='register'),
    path('profile/', never_cache(UserProfileView.as_view()), name='profile'),
    path('verification/<int:pk>/', never_cache(pass_verification), name='verification'),
    path('restore/', never_cache(restore_password), name='restore_password'),
]
