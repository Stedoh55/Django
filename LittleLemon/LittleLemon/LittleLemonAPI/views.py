from django.shortcuts import render

# making the use of Modules from DRF and Not from scratch
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer


# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemview(generics.RetrieveUpdateDestroyAPIView): # For Updating and Deleting an Item
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
