
from django.contrib import admin
from django.urls import path, include
#import settings
from django.conf.urls.static import static
from django.conf import settings
        

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predctive_model.urls', namespace='predctive_model')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)