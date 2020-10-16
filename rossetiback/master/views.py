from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from .models import *


class OrderList(ListView):
    model = Order
    template_name = "master/index.html"


class CreateOrder(CreateView):
    model = Order
    fields = ['place', 'safety_desc']

    def form_valid(self, form):
        return super().form_valid(form)


class OrderDetail(DetailView):
    model = Order
