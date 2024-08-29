from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('admin/', admin.site.urls),
    path('bibliothecaire/', include('bibliothecaire.urls')),
    path('consultation/', include('consultation.urls', namespace='consultation')),
    path('accounts/', include('django.contrib.auth.urls')),
]



