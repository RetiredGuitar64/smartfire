from django.db import models
from django.conf import settings
from django.utils import timezone
from devices.models import Device
class Alarm(models.Model):
    LEVEL_CHOICES=(('low','低'),('medium','中'),('high','高'))
    STATUS_CHOICES=(('active','激活'),('acked','已确认'),('resolved','已解除'))
    device=models.ForeignKey(Device,on_delete=models.CASCADE)
    level=models.CharField(max_length=10,choices=LEVEL_CHOICES,default='low')
    message=models.CharField(max_length=255)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='active')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    cleared_at=models.DateTimeField(null=True,blank=True)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET_NULL)
    class Meta: ordering=['-created_at']
    def __str__(self): return f"{self.device}-{self.message}"
