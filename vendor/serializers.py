from rest_framework import serializers
from .models import Vendors,PurchaseOrder,HistoricalPerformance


class VendorSer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = '__all__'
        

class  PurchaseOrdSer(serializers.ModelSerializer) :
    vendor = serializers.CharField(read_only=True)
    class Meta:
        model = PurchaseOrder
        fields='__all__'

class HistoricalPerformanceSer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = "__all__"

