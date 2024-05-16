from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ViewSet
from .serializers import VendorSer,PurchaseOrdSer,HistoricalPerformanceSer
from .models import Vendors,PurchaseOrder,HistoricalPerformance
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone

# Create your views here.
class VendorViewSet(ModelViewSet):
    
    serializer_class = VendorSer
    queryset=Vendors.objects.all()

    def create(self, request, *args, **kwargs):
        ser = VendorSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"message":"vendor  created successfully"},status=201)
        return Response({"message": "Error", "errors": ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class PurchaseOrderViewSet(ModelViewSet):

    serializer_class = PurchaseOrdSer
    queryset = PurchaseOrder.objects.all()


    def get_queryset(self):
        vendor_id = self.request.query_params.get('vendor_id')
        if vendor_id:
            return PurchaseOrder.objects.filter(vendor_id=vendor_id)
        return PurchaseOrder.objects.all()

    def create(self, request, *args, **kwargs):
        ser = PurchaseOrdSer(data=request.data)
        vendor_id = request.data.get('vendor_id')
        vendor_data = Vendors.objects.get(id=vendor_id)
        if ser.is_valid():
            ser.save(vendor=vendor_data)
            return Response({"message":"Purchase Order created"})
        return Response({"message": "Error", "errors": ser.errors}, status=status.HTTP_400_BAD_REQUEST)


class VendorPerformanceView(APIView):

    def get(self,request,*args,**kwargs):
        try:
            v_id = kwargs.get('vendor_id')
            vendor_performance = HistoricalPerformance.objects.get(vendor=v_id)
            vendor_serializer = HistoricalPerformanceSer(vendor_performance)
            return Response(data=vendor_serializer.data)
        except  HistoricalPerformance.DoesNotExist:
            return Response({"error":"vendor not found"},status=status.HTTP_404_NOT_FOUND)
        

class AcknowledgeView(APIView):

    def post(self,request,*args,**kwargs):
        try:
            po_id = kwargs.get('po_id')
            purchaseorder = PurchaseOrder.objects.get(pk=po_id)
            purchaseorder.acknowledgment_date = timezone.now()
            purchaseorder.save()
            return Response({"Message":"Purchase order Acknowledged"})
        except PurchaseOrder.DoesNotExist:
            return Response({"Error":"purchase order not found"})

            
