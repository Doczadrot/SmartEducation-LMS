from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from users.views import PaymentView

urlpatterns = [
    # Маршрут для админ-панели Django
    path('admin/', admin.site.urls),
    # Маршрут для оплаты
    path('payment/', PaymentView.as_view(), name='payment'),

    # Маршруты для приложения 'materials'
    path('', include('materials.urls')),
    path('users/', include('users.urls')),
    # URL для схемы API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # URL для Свагер UI
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
# Обслуживание медиа-файлов в режиме разработки
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)