from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#Add this For Using Class based views
from rest_framework.views import APIView

#For the Normal Responces without APIs
from django.http import HttpResponse

# Create your views here.
@api_view(['POST'])
def books(request):
    return Response('List of the Books', status=status.HTTP_200_OK)

# Example of the Class Based from view 
class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message":"List of books by " + author}, status.HTTP_200_OK)
        return Response({"message": "List of books"}, status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"message":"new book created"}, status.HTTP_201_CREATED)

# Manipulating a single book item
class Book(APIView):
    def get(self, request, pk):
        return Response({"message":"Single book with id " + str(pk)}, status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)