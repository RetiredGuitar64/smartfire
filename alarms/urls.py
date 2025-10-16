from django.urls import path
from . import views

app_name = "alarms"

urlpatterns = [
    path("", views.alarm_list, name="list"),
    path("<int:pk>/", views.AlarmDetail.as_view(), name="detail"),
    path("add/", views.AlarmCreate.as_view(), name="add"),
    path("<int:pk>/edit/", views.AlarmUpdate.as_view(), name="edit"),
    path("<int:pk>/delete/", views.AlarmDelete.as_view(), name="delete"),
]
