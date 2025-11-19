from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls', namespace='accounts')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('notification/', include('notification.urls', namespace='notification')),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
