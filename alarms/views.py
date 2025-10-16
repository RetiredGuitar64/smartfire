from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Alarm
from .forms import AlarmForm

@login_required
def alarm_list(request):
    f = request.GET.get("status", "").strip()
    qs = Alarm.objects.select_related("device").all().order_by("-id")
    if f:
        qs = qs.filter(status=f)
    return render(request, "alarms/alarm_list.html", {"alarms": qs, "status_filter": f})

class AlarmDetail(LoginRequiredMixin, DetailView):
    model = Alarm
    template_name = "alarms/alarm_detail.html"

class AlarmCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Alarm
    form_class = AlarmForm
    template_name = "alarms/alarm_form.html"
    success_url = reverse_lazy("alarms:list")
    permission_required = "alarms.add_alarm"
    raise_exception = True
    def form_valid(self, form):
        messages.success(self.request, "报警已创建")
        return super().form_valid(form)

class AlarmUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Alarm
    form_class = AlarmForm
    template_name = "alarms/alarm_form.html"
    success_url = reverse_lazy("alarms:list")
    permission_required = "alarms.change_alarm"
    raise_exception = True
    def form_valid(self, form):
        messages.success(self.request, "报警已更新")
        return super().form_valid(form)

class AlarmDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Alarm
    template_name = "alarms/alarm_confirm_delete.html"
    success_url = reverse_lazy("alarms:list")
    permission_required = "alarms.delete_alarm"
    raise_exception = True
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "报警已删除")
        return super().delete(request, *args, **kwargs)
