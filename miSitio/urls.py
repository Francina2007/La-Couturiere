
from django.contrib import admin
from django.urls import path,include
from MODA.views import mostrar_reseñas
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('', include('MODA.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
