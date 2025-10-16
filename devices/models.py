from django.db import models
class Device(models.Model):
    STATUS_CHOICES = (('normal','正常'),('fault','故障'),('offline','离线'))
    name = models.CharField(max_length=100, unique=True)
    device_type = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='normal')
    installed_at = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    class Meta: ordering = ['name']
    def __str__(self): return f"{self.name}-{self.location}"
