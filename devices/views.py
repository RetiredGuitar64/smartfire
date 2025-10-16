from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Device
from .forms import DeviceForm

@login_required
def device_list(request):
    q = request.GET.get("q", "").strip()
    qs = Device.objects.all().order_by("-id")
    if q:
        qs = qs.filter(name__icontains=q) | qs.filter(device_type__icontains=q) | qs.filter(location__icontains=q)
    return render(request, "devices/device_list.html", {"devices": qs, "q": q})

class DeviceDetail(LoginRequiredMixin, DetailView):
    model = Device
    template_name = "devices/device_detail.html"

class DeviceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm
    template_name = "devices/device_form.html"
    success_url = reverse_lazy("devices:list")
    permission_required = "devices.add_device"
    raise_exception = True
    def form_valid(self, form):
        messages.success(self.request, "设备已创建")
        return super().form_valid(form)

class DeviceUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = "devices/device_form.html"
    success_url = reverse_lazy("devices:list")
    permission_required = "devices.change_device"
    raise_exception = True
    def form_valid(self, form):
        messages.success(self.request, "设备已更新")
        return super().form_valid(form)

class DeviceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Device
    template_name = "devices/device_confirm_delete.html"
    success_url = reverse_lazy("devices:list")
    permission_required = "devices.delete_device"
    raise_exception = True
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "设备已删除")
        return super().delete(request, *args, **kwargs)
