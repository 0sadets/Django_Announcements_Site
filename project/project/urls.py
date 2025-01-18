from django.contrib import admin
from django.urls import path
from announcements import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.index),
    path("list/<int:id>", views.list, name='list'),
    path("delete/<int:id>", views.delete, name='delete'),
]
