from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder,Vendors,HistoricalPerformance
from django.db.models import Count,F,Avg
from datetime  import datetime

@receiver(post_save,sender=PurchaseOrder)
def update_vendor_performance_on_po_save(sender,instance,created,**kwargs):
    if not created:
        update_vendor_perfomance(instance.vendor)

def update_vendor_perfomance(vendor):
    vendor.on_time_delivery_rate = calculate_on_time_delivery_rate(vendor) 
    vendor.quality_rating_avg = calculate_quality_rating_avg(vendor)
    vendor.average_response_time = calculate_average_response_time(vendor)
    vendor.fulfilment_rate = calculate_fulfilment_rate(vendor)
    vendor.save()
    update_historical_performance(vendor)

def update_historical_performance(vendor):
    historical_performance, created = HistoricalPerformance.objects.update_or_create(
        vendor=vendor,
        defaults={
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
             'quality_rating_avg': vendor.quality_rating_avg,
             'avg_response_time' : vendor.avg_response_time,
             'fulfilment_rate'  : vendor.fulfilment_rate

        }
    )
    historical_performance.save()

def calculate_on_time_delivery_rate(vendor):
    
    completed_purchases=PurchaseOrder.objects.filter(vendor=vendor,status='Completed',
                                                     delivery_date__lte=F('acknowledgment_date')).count()
    total_completed_orders=PurchaseOrder.objects.filter(vendor=vendor,status='Completed').count()
    if total_completed_orders > 0:
        on_time_delivery_rate=completed_purchases / total_completed_orders
        # print(on_time_delivery_rate)
    else:
        on_time_delivery_rate = 0.0

    return on_time_delivery_rate

def calculate_quality_rating_avg(vendor):
    quality_rating=PurchaseOrder.objects.filter(vendor=vendor,
                                                status='Completed').aggregate(Avg("quality_rating"))
    if quality_rating:
        quality_rating_avg = quality_rating.get('quality_rating__avg')
        return quality_rating_avg
    return 0

def calculate_average_response_time(vendor):
    total_response_time = 0
    total_orders = 0

    completed_pos = PurchaseOrder.objects.filter(vendor=vendor,
                                                 status='Completed',
                                                 acknowledgment_date__isnull=False)
    
    for po in completed_pos:
        if po.acknowledgment_date and po.issue_date:
            response_time=po.acknowledgment_date - po.issue_date
            total_response_time +=response_time
            total_orders += 1

    if total_orders > 0:
        avg_response_time=total_response_time / total_orders
    else:
        avg_response_time = 0

    return avg_response_time

def calculate_fulfilment_rate(vendor):
    # Fulfilled orders are those that have been completed

    completed_po_count = PurchaseOrder.objects.filter(vendor=vendor,status='Completed').count()
    print('completed po count',completed_po_count)
    po_count = PurchaseOrder.objects.filter(vendor=vendor).count()
    # print('po_count',po_count)

    if po_count > 0:
        fulfilment_rate= completed_po_count / po_count

    else:
        fulfilment_rate = 0
    # print('fulfilment_rate',fulfilment_rate)
    return fulfilment_rate


