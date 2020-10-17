from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('get_orders/', views.GetOrders.as_view(), name='get_orders'),
    path('obtain_token/', obtain_auth_token, name='api_token_auth'),
]
