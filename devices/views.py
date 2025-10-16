from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Device
from .forms import DeviceForm
def is_admin(u): return u.is_authenticated and u.is_staff
@login_required
def device_list(request):
    q=request.GET.get('q','')
    devices=Device.objects.all()
    if q: devices=devices.filter(Q(name__icontains=q)|Q(device_type__icontains=q)|Q(location__icontains=q))
    return render(request,'devices/device_list.html',{'devices':devices,'q':q})
@login_required
@user_passes_test(is_admin)
def device_create(request):
    form=DeviceForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save();return redirect('devices:list')
    return render(request,'devices/device_form.html',{'form':form,'title':'新增设备'})
@login_required
@user_passes_test(is_admin)
def device_update(request,pk):
    d=get_object_or_404(Device,pk=pk)
    form=DeviceForm(request.POST or None,instance=d)
    if request.method=='POST' and form.is_valid():
        form.save();return redirect('devices:list')
    return render(request,'devices/device_form.html',{'form':form,'title':'编辑设备'})
@login_required
@user_passes_test(is_admin)
def device_delete(request,pk):
    d=get_object_or_404(Device,pk=pk)
    if request.method=='POST':d.delete();return redirect('devices:list')
    return render(request,'devices/device_confirm_delete.html',{'device':d})
