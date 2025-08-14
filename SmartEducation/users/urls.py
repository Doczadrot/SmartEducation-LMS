
from django.urls import path
from .views import PaysListAPIView # Импортируем наше представление

urlpatterns = [
    path('pays/', PaysListAPIView.as_view(), name='pays_list'),
]