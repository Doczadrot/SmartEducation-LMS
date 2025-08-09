from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet

router = DefaultRouter()

# Регистрируем CourseViewSet
router.register(r'courses', CourseViewSet, basename='courses')

# Регистрируем LessonViewSet
router.register(r'lessons', LessonViewSet, basename='lessons')


urlpatterns = router.urls