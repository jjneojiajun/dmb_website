from rest_framework import serializers

from .models import BankRates


class BankRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankRates
        fields = '__all__'
