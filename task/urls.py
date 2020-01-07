from django.urls import path
from task import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static 
details_new

app_name = 'task'

urlpatterns = [
    path('', views.details_new, name='details_new'),
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 