from .models import *
from rest_framework import serializers
# from rest_framework.serializers import

class DailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model=DailyPrice
        fields='__all__'