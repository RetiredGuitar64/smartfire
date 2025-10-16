from django.urls import path
from . import views
app_name='alarms'
urlpatterns=[
    path('',views.alarm_list,name='list'),
    path('<int:pk>/',views.alarm_detail,name='detail'),
    path('create/',views.alarm_create,name='create'),
    path('<int:pk>/edit/',views.alarm_edit,name='edit'),
    path('<int:pk>/status/<str:status_value>/',views.alarm_set_status,name='set_status'),
    path('status-json/',views.alarm_status_json,name='status_json'),
]
