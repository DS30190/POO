from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [

    path('admin/', admin.site.urls),
    path('bibliothecaire/', include('bibliothecaire.urls')),
    path('consultation/', include('consultation.urls')),
]


