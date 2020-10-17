from django.shortcuts import render
from django.http import JsonResponse

from common.models import *


def main(request):
    if request.method == 'GET':
        worker = Worker.objects.all()[0]
        order = Order.objects.filter(electrician=worker).filter(active=True).all()[0]
        resp = {}
        resp['order_num'] = order.order_num
        return JsonResponse(resp, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'POST':
        pass
