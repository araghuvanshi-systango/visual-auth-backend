from django.urls import path
from django.contrib import admin

from visual_auth import views
from websocket.urls import websocket


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.visual_feed),
    websocket("ws/", views.visual_feed_api),
]
