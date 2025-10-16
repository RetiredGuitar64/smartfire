from django.urls import path
from . import views

app_name = "alarms"

urlpatterns = [
    path("", views.alarm_list, name="list"),
    path("add/", views.AlarmCreateView.as_view(), name="add"),
    path("<int:pk>/edit/", views.AlarmUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.AlarmDeleteView.as_view(), name="delete"),
]
