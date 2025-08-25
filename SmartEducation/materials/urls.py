from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, SubscriptionAPIView

router = DefaultRouter()

# Регистрируем CourseViewSet
router.register(r'courses', CourseViewSet, basename='courses')

# Регистрируем LessonViewSet
router.register(r'lessons', LessonViewSet, basename='lessons')
# Регистрируем  Subscrip
sub_urlpatterns = [
    path('subscription/', SubscriptionAPIView.as_view(), name='subscription'),
]

urlpatterns = router.urls + sub_urlpatterns