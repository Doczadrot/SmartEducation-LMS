from rest_framework import viewsets
from rest_framework.permissions import AllowAny # Импортируем класс разрешений
from .models  import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    # Устанавливаем набор данных (все объекты модели Course)
    queryset = Course.objects.all()
    # Указываем, какой сериализатор будет использоваться для обработки данных
    serializer_class = CourseSerializer
    # Разрешаем доступ к этому представлению для любого пользователя (даже неаутентифицированного)
    permission_classes = (AllowAny,)

class LessonViewSet(viewsets.ModelViewSet):
    # Устанавливаем набор данных (все объекты модели Lesson)
    queryset = Lesson.objects.all()
    # Указываем, какой сериализатор будет использоваться
    serializer_class = LessonSerializer
    # Разрешаем доступ для любого пользователя
    permission_classes = (AllowAny,)