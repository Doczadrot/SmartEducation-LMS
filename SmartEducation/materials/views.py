from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated  # Импортируем класс разрешений
from .models  import Course, Lesson
from .serializers import LessonSerializer, CourseDetailSerializer

# noinspection PyUnresolvedReferences
from users.permissions import IsNotModerator, ControlModerator, IsOwnerOrReadOnly


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

    def get_permissions(self):
        # Пользователь может только просматривать (list, retrieve),
        # если он модератор
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny] # Разрешаем просмотр всем

        elif self.action == "destroy":
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

        elif self.action in ["create"]:
            # Создавать могут только авторизованные, не модераторы
            permission_classes = [IsAuthenticated, IsNotModerator]


        elif self.action in ["update", "partial_update", "destroy"]:
            # Редактировать и удалять могут модераторы или владельцы
            permission_classes = [IsAuthenticated, ControlModerator | IsOwnerOrReadOnly]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        elif self.action in ["create"]:
            # Создавать могут только авторизованные, не модераторы
            permission_classes = [IsAuthenticated, IsNotModerator]
        elif self.action == "destroy":
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        elif self.action in ["update", "partial_update", "destroy"]:
            # Редактировать и удалять могут модераторы или владельцы

            permission_classes = [IsAuthenticated, ControlModerator | IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)