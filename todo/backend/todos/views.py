from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics

# Create your views here.
# Retrieving all the records (Collection API)
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Retrieving an istance based on primary key
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
