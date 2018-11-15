from .models import BankRates
from .serializers import BankRatesSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.http import HttpResponse
from django.template.loader import get_template


class BankFilter(filters.FilterSet):
    lower_interest_rate = filters.NumberFilter(field_name="interest_rates", lookup_expr='lte')

    class Meta:
        model = BankRates
        fields = ['loan_type', 'lower_interest_rate']


class BankRatesViewSet(viewsets.ModelViewSet):
    queryset = BankRates.objects.all()
    serializer_class = BankRatesSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_class = BankFilter


