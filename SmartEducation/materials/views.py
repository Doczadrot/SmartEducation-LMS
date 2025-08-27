from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Course, Lesson, Subscription
from .paginators import CursePaginator
from .serializers import LessonSerializer, CourseDetailSerializer, SubscriptionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import IsNotModerator, IsOwnerOrReadOnly, IsModeratorOrOwner
from users.models import Pays
from .tasks import subscription_course_mail


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    pagination_class = CursePaginator

    def perform_update(self, serializer):
        instance = serializer.save()
        subscription_course_mail.delay(instance.id)

    def get_permissions(self):
        # Разрешаем просмотр списка и отдельного объекта всем
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        # Создавать могут только авторизованные, не модераторы
        elif self.action == "create":
            permission_classes = [IsAuthenticated, IsNotModerator]
        # Редактировать могут модераторы или владельцы
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsAuthenticated, IsModeratorOrOwner]
        # Удалять могут только владельцы
        elif self.action == "destroy":
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CursePaginator

    def get_permissions(self):
        # Разрешаем просмотр списка и отдельного объекта всем
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        # Создавать могут только авторизованные, не модераторы
        elif self.action == "create":
            permission_classes = [IsAuthenticated, IsNotModerator]
        # Редактировать могут модераторы или владельцы
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsAuthenticated, IsModeratorOrOwner]
        # Удалять могут только владельцы
        elif self.action == "destroy":
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer #для того что бы drf-spectacular прочитал наш сериализатор

    def post(self, request):
        user = request.user
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, id=course_id)

        try:
            subscription = Subscription.objects.get(user=user, course=course)
            subscription.delete()
            return Response({'message': 'Подписка удалена'}, status=200)
        except Subscription.DoesNotExist:
            Subscription.objects.create(user=user, course=course)
            return Response({'message': 'Подписка создана'}, status=201)