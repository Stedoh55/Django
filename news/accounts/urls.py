from django.urls import path
from .views import SignUpView,logout_request

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", logout_request, name='logout')
    
   
    
    
]
