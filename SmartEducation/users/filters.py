import django_filters
from django_filters.rest_framework import FilterSet

from .models import Pays

class PaysFilter(FilterSet):

    class Meta:
        model = Pays
        fields = ('date', 'paid_course', 'paid_lesson', 'variant_pays') #указываем по каким полям нужно фильтровать
