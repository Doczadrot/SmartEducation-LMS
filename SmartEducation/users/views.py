
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter # Для сортировки
from django_filters.rest_framework import DjangoFilterBackend # Для фильтрации
from rest_framework.permissions import IsAuthenticated

from .models import Pays
from .serializers import PaysSerializer
from .filters import PaysFilter # Импортируем наш класс фильтра

class PaysListAPIView(ListAPIView):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter) # Добавляем бэкенды фильтрации и сортировки
    filterset_class = PaysFilter # Указываем наш класс фильтра
    ordering_fields = ('date',) # Указываем поле, по которому можно сор
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Pays.objects.filter(user=self.request.user)