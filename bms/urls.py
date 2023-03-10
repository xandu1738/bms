from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('records.urls')),
    path('api/', include('api.urls')),
    path('management/', include('management.urls')),
    path('management/', include('django.contrib.auth.urls')),
]
