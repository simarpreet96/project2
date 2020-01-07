from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.contrib.auth import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header="simar1"
admin.site.site_title="simar2"
admin.site.index_title= "simar3"
