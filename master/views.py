from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.utils import timezone as tz
from datetime import timezone, datetime

from common.models import *


class OrderList(ListView):
    model = Order
    template_name = "master/order_list.html"


class CreateOrder(CreateView):
    model = Order
    fields = ['order_num', 'organization', 'subdivision', 'object', 'safety_desc', 'electrician']
    template_name = "master/order_form.html"

    def form_valid(self, form):
        form.instance.master = self.request.user.worker
        form.instance.instructions_given = datetime.timestamp(tz.now())
        return super().form_valid(form)


class OrderDetail(DetailView):
    model = Order
    template_name = "master/order_detail.html"


class ReportList(ListView):
    model = Report
    template_name = "master/report_list.html"


class ReportDetail(DetailView):
    model = Report
    template_name = "master/report_detail.html"
