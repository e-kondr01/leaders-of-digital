from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView
from django.utils import timezone as tz
from datetime import timezone, datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from common.models import *


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = "master/order_list.html"


class CreateOrder(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['order_num', 'organization', 'subdivision', 'object', 'safety_desc', 'electrician']
    template_name = "master/order_form.html"

    def form_valid(self, form):
        form.instance.master = self.request.user.worker
        form.instance.instructions_given = datetime.timestamp(tz.now())
        return super().form_valid(form)


class OrderDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "master/order_detail.html"


class ReportList(LoginRequiredMixin, ListView):
    model = Report
    template_name = "master/report_list.html"


class ReportDetail(LoginRequiredMixin, DetailView):
    model = Report
    template_name = "master/report_detail.html"


@login_required
def receive_report(request, pk):
    report = Report.objects.get(pk=pk)
    report.received_by = request.user.worker
    report.received_at = datetime.timestamp(tz.now())
    return HttpResponseRedirect(reverse('report_detail', kwargs={'pk': pk}))
