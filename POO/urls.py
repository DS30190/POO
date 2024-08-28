from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('bibliothecaire/', include('bibliothecaire.urls')),
    path('consultation/', include('consultation.urls')),
]


