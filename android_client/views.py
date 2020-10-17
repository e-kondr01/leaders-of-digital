from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

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
            data['latitude'] = subobject.latitude
            data['longitude'] = subobject.longitude
            resp['subobjects'].append(data)
        return Response(resp)


class SubmitOrderData(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk=0):
        order_pk = request.data['order_id']
        order = Order.objects.get(pk=order_pk)

        report = Report(order=order)

        job_started = request.data['job_started'] // 1000
        job_started_dt = datetime.fromtimestamp(job_started, tz=datetime.tzinfo.tzname('utc'))
        order.job_started = job_started_dt
        order.instructions_received = job_started_dt
        job_finished = request.data['job_finished'] // 1000
        job_finished_dt = datetime.fromtimestamp(job_finished, tz=datetime.tzinfo.tzname('utc'))
        order.job_finished = job_finished_dt
        order.active = False

        defects = request.data['defects']
        for defect in defects:
            if defect['defect_type_id'] != 1:
                pass

        report.save()
        order.save()
        resp = 'success'
        return Response(resp)
