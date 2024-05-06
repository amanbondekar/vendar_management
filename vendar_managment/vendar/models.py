from django.db import models
from django.db.models import Count, Avg
from datetime import timedelta

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    response_time_avg = models.FloatField(default=0)
    fulfilment_rate = models.FloatField(default=0)

    def update_performance_metrics(self):
        completed_pos = self.purchaseorder_set.filter(status='completed')
        total_completed_pos = completed_pos.count()

        # On-Time Delivery Rate
        on_time_deliveries = completed_pos.filter(delivery_date__lte=models.F('issue_date'))
        on_time_delivery_rate = (on_time_deliveries.count() / total_completed_pos) * 100 if total_completed_pos > 0 else 0
        self.on_time_delivery_rate = on_time_delivery_rate

        # Quality Rating Average
        quality_rating_avg = completed_pos.aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']
        self.quality_rating_avg = quality_rating_avg if quality_rating_avg is not None else 0

        # Average Response Time
        response_time_avg = completed_pos.aggregate(avg_response_time=Avg(models.F('acknowledgment_date') - models.F('issue_date')))['avg_response_time']
        self.response_time_avg = response_time_avg.total_seconds() / total_completed_pos if response_time_avg is not None else 0

        # Fulfilment Rate
        fulfilled_pos = completed_pos.exclude(status='completed with issues')
        fulfilment_rate = (fulfilled_pos.count() / self.purchaseorder_set.count()) * 100 if self.purchaseorder_set.count() > 0 else 0
        self.fulfilment_rate = fulfilment_rate

        self.save()

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == 'completed':
            self.vendor.update_performance_metrics()

    def __str__(self):
        return self.po_number
