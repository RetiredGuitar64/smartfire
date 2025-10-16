from django.urls import path
from . import views

app_name = "devices"

urlpatterns = [
    path("", views.device_list, name="list"),
    path("add/", views.DeviceCreateView.as_view(), name="add"),
    path("<int:pk>/edit/", views.DeviceUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.DeviceDeleteView.as_view(), name="delete"),
]
