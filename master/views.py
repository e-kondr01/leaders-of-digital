from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.utils import timezone

from common.models import *


class OrderList(ListView):
    model = Order
    template_name = "master/index.html"


class CreateOrder(CreateView):
    model = Order
    fields = ['order_num', 'organization', 'subdivision', 'object', 'safety_desc', 'electrician']
    template_name = "master/order_form.html"

    def form_valid(self, form):
        form.instance.master = self.request.user.worker
        form.instance.instructions_received = datetime.timestamp(timezone.now())
        return super().form_valid(form)


class OrderDetail(DetailView):
    model = Order
    template_name = "master/order_detail.html"
