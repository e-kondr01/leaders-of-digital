from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('get_orders/', views.GetOrders.as_view(), name='get_orders'),
    path('get_order_info/<int:pk>', views.GetOrderInfo.as_view(), name='get_order_info'),
    path('obtain_token/', obtain_auth_token, name='api_token_auth'),
]
