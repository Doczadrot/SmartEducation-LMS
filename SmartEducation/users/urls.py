from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views import PaysListAPIView, UserRegistrationViewSet, UserViewSet

router = DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='register')
router.register(r'user', UserViewSet, basename='users')

urlpatterns = [
    path('pays/', PaysListAPIView.as_view(), name='pays_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

   #Маршрут регистрации
    path('', include(router.urls)),
]