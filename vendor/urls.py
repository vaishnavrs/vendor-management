from django.urls import path
from  .views import VendorViewSet,PurchaseOrderViewSet,VendorPerformanceView,AcknowledgeView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('vendors',VendorViewSet,basename='vendor')
router.register('purchase_orders',PurchaseOrderViewSet,basename='purchase')

urlpatterns=[
    path('vendors/<int:vendor_id>/performance',VendorPerformanceView.as_view(),name = 'performance'),
    path('purchase_orders/<int:po_id>/acknowledgment_date',AcknowledgeView.as_view(),name = 'ack')    
]+router.urls