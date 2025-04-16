from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home),
    path('menu-items', views.MenuItemsViewSet.as_view({'get':'list'})),
    path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get':'retrieve'})),
    # path('menu-items', views.menu_items),
    path('secret', views.secret),
    path('api-token-auth/', obtain_auth_token),  #Generating Auth Token
    path('secret', views.secret), 
    path('manager-view', views.manager_view),    #Only Authenticated Users under manager group can visit this endpoint
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check_auth), 
    path('blog', views.form_view),
    path('api/sample', views.sample_api),
]
