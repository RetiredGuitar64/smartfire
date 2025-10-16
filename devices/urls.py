from django.urls import path
from . import views

app_name = "devices"

urlpatterns = [
    path("", views.device_list, name="list"),
    path("<int:pk>/", views.DeviceDetail.as_view(), name="detail"),
    path("add/", views.DeviceCreate.as_view(), name="add"),
    path("<int:pk>/edit/", views.DeviceUpdate.as_view(), name="edit"),
    path("<int:pk>/delete/", views.DeviceDelete.as_view(), name="delete"),
]
