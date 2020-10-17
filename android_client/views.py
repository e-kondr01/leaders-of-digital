from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from common.models import *


class GetOrders(APIView):
    permission_classes = (IsAuthenticated,)  

    def get(self, request):
        worker = Worker.objects.get(user=request.user)
        orders = Order.objects.filter(electrician=worker).filter(active=True).all()
        resp = []
        for order in orders:
            order_info = {}
            order_info['order_id'] = order.pk
            order_info['order_num'] = order.order_num
            order_info['place'] = str(order.object) + order.range
            order_info['description'] = order.safety_desc
            order_info['master'] = order.master
            resp.append(order_info)
        return Response(resp)


def obtain_id(request):
    if request.user.is_authenticated:
        resp = {'user_id': request.user.id}
    else:
        resp = {'error': 'user not authenticated'}
    return JsonResponse(resp)
