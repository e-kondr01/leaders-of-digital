from django.urls import path

from . import views

urlpatterns = [
    path('order/', views.main, name='main'),
]
