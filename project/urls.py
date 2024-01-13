from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviewform.urls')),
    path('problems/', include('problems.urls')),
    path('users/', include('users.urls', namespace="users")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
