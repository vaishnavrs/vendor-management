from django.contrib import admin
from .models import PurchaseOrder,HistoricalPerformance,Vendors
# Register your models here.

admin.site.register(HistoricalPerformance)
admin.site.register(PurchaseOrder)
