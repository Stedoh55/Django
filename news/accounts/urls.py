from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView # new
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", TemplateView.as_view(template_name="home.html"),name="home"),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('accounts/logout/', LogoutView.as_view(), name='logout')
    
]
