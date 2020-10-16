from django.urls import path

from . import views

urlpatterns = [
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('order/create', views.CreateOrder.as_view(), name='create_order'),
    path("", views.OrderList.as_view(), name="index"),
]
