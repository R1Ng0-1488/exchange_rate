from rest_framework import serializers
from .models import USDRate


class USDRateSerializer(serializers.ModelSerializer):
	class Meta:
		model = USDRate
		fields = ['usd']
