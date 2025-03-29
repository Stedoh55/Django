#1. making the use of Modules from DRF and Not from scratch(Class based View)
from django.shortcuts import render
from LittleLemonAPI.forms import CommentForm
from .models import UserComment
from django.http import JsonResponse
from datetime import datetime

from rest_framework import generics #Used in Approach Number 1
from rest_framework import viewsets #Used in approach Number 3
from .models import MenuItem
from .serializers import MenuItemSerializer

#2. Enabling Search and Filter Functionality(Function Based Approach)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, throttle_classes  #For use with Throttling
from rest_framework import status

#2. Enabling pagination(FUnction Based Approach)
from django.core.paginator import Paginator, EmptyPage

#4.  For Enabling Authentications(Token Protected)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

#6. For Enabling Throttling
from rest_framework.throttling import AnonRateThrottle      #For Anonymous User
from rest_framework.throttling import UserRateThrottle      #For Authenticated Users
from .throttles import TenCallsPerMinute



# Create your views here.

# 1. Using the Normal Data Retrieval(Class Based View)
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# class SingleMenuItemview(generics.RetrieveUpdateDestroyAPIView): # For Updating and Deleting an Item
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# Welcome Page
def home(request):
    return render(request, 'index.html')


#2. Using the Search functionalities (Function Based Approach)
@api_view(['GET','POST'])
def menu_items(request):
    if(request.method=='GET'):
        items = MenuItem.objects.select_related('category').all()   #Applying the filter by Category on Data Retrieval
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=5)    # When number isn't provided, default is 2
        page = request.query_params.get('page', default=1)

        if category_name:                                           #Applying the filter by the  Category name
            items = items.filter(category__title = category_name)
        
        if to_price:                                                #Applying filter by Price
            items = items.filter(price__lte=to_price)

        if search:                                                  #Applying search functionality case insensitive
            items = items.filter(title__icontains=search)
        
        if ordering:                                                # Multiple factor ordering using comma separator
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    
    elif(request.method=='POST'):
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)


# 3. Using Filtering, Searching, Ordering and Pagination in Class Based Approach
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields=['price', 'inventory']
    search_fields=['title']

#4. Enabling the Token Protected API endpoints
@api_view()
@permission_classes({IsAuthenticated})
def secret(request):
    return Response({"message":"Some Secret message"})

#5. Enabling the the User Roles as the Manager
@api_view()
@permission_classes({IsAuthenticated})
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({"message":"Only manager Should See this"})
    else:
        return Response({"message":"You are not authorized as the Manager"}, 403)
    
#6. Enabling Throttling to prevent API endpoints abuse
    # A:For Anonymous Users
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"Successful"})

    #B:For Authenticated Users
@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute ])
def throttle_check_auth(request):
    return Response({"message":"Successful Your Are in Authenticated Mode"})


# Views for The User comments
def form_view(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uc = UserComment(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment'],
            )
            uc.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'blog.html',{'form': form} )


    