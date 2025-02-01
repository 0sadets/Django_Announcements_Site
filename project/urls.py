from django.contrib import admin
from django.urls import include, path
from announcements import views
from django.conf.urls.static import static

from project import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("announcements.urls")),
]

# if settings:  # Only serve media files in development
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)