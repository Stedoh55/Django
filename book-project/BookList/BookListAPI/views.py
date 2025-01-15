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
        return Response({"message":"list of books"}, status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"message":"new book created"}, status.HTTP_201_CREATED)