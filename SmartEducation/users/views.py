
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.filters import OrderingFilter # Для сортировки
from django_filters.rest_framework import DjangoFilterBackend # Для фильтрации
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Users
from .serializers import UserRegistrationSerializer, UserSerializer

from .models import Pays
from .serializers import PaysSerializer
from .filters import PaysFilter # Импортируем наш класс фильтра
from materials.models import Course
from materials.serveces import create_stripe_price, create_stripe_pay

class PaysListAPIView(ListAPIView):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter) # Добавляем бэкенды фильтрации и сортировки
    filterset_class = PaysFilter # Указываем наш класс фильтра
    ordering_fields = ('date',) # Указываем поле, по которому можно сортировать
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Pays.objects.filter(user=self.request.user)


class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class PaymentView(APIView):
    def post(self, request):

        course = get_object_or_404(Course, pk=request.data.get('course_id'))
        #Cоздание цены
        stripe_price = create_stripe_price(course)
        create_stripe_pay_url =  create_stripe_pay(stripe_price.id)#Создаю оплату
        new_pay = Pays(user=request.user, paid_course=course, payment_urls=create_stripe_pay_url) #добавляю созданую ссылуку в бд
        new_pay.save() #сохраняю ссылку
        return Response({'url': create_stripe_pay_url})#Возвращаю url клиену