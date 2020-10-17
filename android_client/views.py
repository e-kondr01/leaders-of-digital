from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from common.models import *


class GetOrders(APIView):
    permission_classes = (IsAuthenticated,)  

    def get(self, request):
        worker = Worker.objects.all()[0]
        order = Order.objects.filter(electrician=worker).filter(active=True).all()[0]
        resp = {}
        resp['order_num'] = order.order_num
        return Response(resp)


def obtain_id(request):
    if request.user.is_authenticated:
        resp = {'user_id': request.user.id}
    else:
        resp = {'error': 'user not authenticated'}
    return JsonResponse(resp)
