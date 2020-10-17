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
            order_info['place'] = str(order.object)
            order_info['latitude'] = str(order.object.latitude)
            order_info['longitude'] = str(order.object.longitude)
            order_info['description'] = order.safety_desc
            order_info['master'] = str(order.master)
            resp.append(order_info)
        return Response(resp)


class GetOrderInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=0):
        order = Order.objects.get(pk=pk)
        subobjects = order.object.subobjects.all()
        defects = DefectType.objects.all()

        resp = {}
        resp['defect_types'] = []
        resp['subobjects'] = []

        for defect in defects:
            data = {}
            data['defect_type_id'] = defect.pk
            data['defect_type_description'] = str(defect)
            resp['defect_types'].append(data)
        for subobject in subobjects:
            data = {}
            data['subobject_id'] = subobject.pk
            data['subobject_description'] = str(subobject)
            resp['subobjects'].append(data)
        return Response(resp)


class SubmitOrderData(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=0):
        order = Order.objects.get(pk=pk)
        subobjects = order.object.subobjects.all()
        defects = DefectType.objects.all()

        resp = {}
        resp['defect_types'] = {}
        resp['subobjects'] = {}

        for defect in defects:
            resp['defect_types'][defect.pk] = str(defect)
        for subobject in subobjects:
            resp['subobjects'][subobject.pk] = str(subobject)
        return Response(resp)
