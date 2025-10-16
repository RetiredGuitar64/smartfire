from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('devices/', include('devices.urls')),
    path('alarms/', include('alarms.urls')),
    path('stats/', include('stats.urls')),
    path('', RedirectView.as_view(url='/stats/dashboard/', permanent=False)),
]
