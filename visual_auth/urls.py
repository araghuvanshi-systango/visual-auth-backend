from django.contrib import admin
from django.urls import path

from visual_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.visual_feed)
]
