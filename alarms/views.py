from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import Alarm
from .forms import AlarmForm
def is_admin(u): return u.is_authenticated and u.is_staff
@login_required
def alarm_list(request):
    f=request.GET.get('status','');qs=Alarm.objects.select_related('device')
    if f in dict(Alarm.STATUS_CHOICES):qs=qs.filter(status=f)
    return render(request,'alarms/alarm_list.html',{'alarms':qs,'status_filter':f})
@login_required
def alarm_detail(request,pk):
    a=get_object_or_404(Alarm,pk=pk)
    return render(request,'alarms/alarm_detail.html',{'alarm':a})
@login_required
@user_passes_test(is_admin)
def alarm_create(request):
    form=AlarmForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        a=form.save(commit=False)
        if a.status=='resolved' and not a.cleared_at:a.cleared_at=timezone.now()
        a.save();return redirect('alarms:list')
    return render(request,'alarms/alarm_form.html',{'form':form,'title':'新增报警'})
@login_required
@user_passes_test(is_admin)
def alarm_edit(request,pk):
    a=get_object_or_404(Alarm,pk=pk)
    form=AlarmForm(request.POST or None,instance=a)
    if request.method=='POST' and form.is_valid():
        form.save();return redirect('alarms:detail',pk=pk)
    return render(request,'alarms/alarm_form.html',{'form':form,'title':'编辑报警'})
@login_required
@user_passes_test(is_admin)
def alarm_set_status(request,pk,status_value):
    a=get_object_or_404(Alarm,pk=pk)
    if status_value not in dict(Alarm.STATUS_CHOICES):return redirect('alarms:detail',pk=pk)
    a.status=status_value
    if status_value=='resolved' and not a.cleared_at:a.cleared_at=timezone.now()
    a.save(update_fields=['status','cleared_at','updated_at'])
    return redirect('alarms:detail',pk=pk)
@login_required
def alarm_status_json(request):
    total=Alarm.objects.count()
    active=Alarm.objects.filter(status='active').count()
    acked=Alarm.objects.filter(status='acked').count()
    resolved=Alarm.objects.filter(status='resolved').count()
    return JsonResponse({'total':total,'active':active,'acked':acked,'resolved':resolved})
