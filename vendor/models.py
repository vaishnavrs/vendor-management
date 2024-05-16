from django.db import models

# Create your models here.
class Vendors(models.Model):

    name = models.CharField(max_length=100)
    address = models.TextField()
    vendor_code = models.CharField(max_length=20,unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0,null=True)
    avg_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendors,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True,null=True)
    items = models.JSONField(default=dict)
    quantity = models.IntegerField(default=0)
    options = (
        ('Pending','Pending'),
        ('Completed','Completed'),
        ('Canceled','Canceled')
    )
    status = models.CharField(max_length=100,choices=options,default='Pending')
    quality_rating = models.FloatField(default=0,null=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    acknowledgment_date = models.DateTimeField(blank=True, null=True)



class HistoricalPerformance(models.Model):

    vendor = models.ForeignKey(Vendors,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0)
    avg_response_time = models.FloatField(default=0)
    fulfilment_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0,null=True)
