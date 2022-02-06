from rest_framework import serializers
from .models import BTCPrice

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTCPrice
        fields = ('id', 'price')
        read_only_fields = ('id',)
        