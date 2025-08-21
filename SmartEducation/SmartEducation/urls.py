from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Маршрут для админ-панели Django
    path('admin/', admin.site.urls),

    # Маршруты для приложения 'materials'
    path('', include('materials.urls')),
    path('users/', include('users.urls')),
]

# Обслуживание медиа-файлов в режиме разработки
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)