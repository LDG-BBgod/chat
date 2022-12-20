from django.contrib import admin
from django.urls import include, path
from chat.views import index, room

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/", index),
    path("chat/<str:room_name>/", room),
]