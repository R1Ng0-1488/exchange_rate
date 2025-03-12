from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from .models import USDRate
from .serializers import USDRateSerializer

import requests


class GetUsdRateView(APIView):

	def get(self, request, format=None):
		try:
			r = requests.get(f'https://{settings.URL}/v6/{settings.KEY}/latest/USD')
			rub = r.json()['conversion_rates']['RUB']
			USDRate.objects.create(usd=f'{rub} рублей')
			models = USDRate.objects.order_by('-created')[:10]
			serializer = USDRateSerializer(models, many=True)
		except Exception as e:
			return Response([])
		return Response(serializer.data)