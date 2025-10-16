from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from devices.models import Device
from alarms.models import Alarm
@login_required
def dashboard(request):
    device_counts={'normal':Device.objects.filter(status='normal').count(),
                   'fault':Device.objects.filter(status='fault').count(),
                   'offline':Device.objects.filter(status='offline').count()}
    alarm_counts={'active':Alarm.objects.filter(status='active').count(),
                  'acked':Alarm.objects.filter(status='acked').count(),
                  'resolved':Alarm.objects.filter(status='resolved').count()}
    latest_alarms=Alarm.objects.select_related('device')[:10]
    return render(request,'stats/dashboard.html',{'device_counts':device_counts,'alarm_counts':alarm_counts,'latest_alarms':latest_alarms})
