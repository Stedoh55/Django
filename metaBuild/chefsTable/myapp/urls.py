from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/', views.about),
    path('menu/', views.usambara_menu),
    path('form/', views.our_form),

]
