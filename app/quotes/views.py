from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import parsers, renderers, status
import requests

from .models import BTCPrice
from .serializers import PriceSerializer
from django.conf import settings


api_key = settings.API_KEY
api_url = settings.ALPHADANTAGE_API_URL


class GetPrice(APIView):
    permission_classes = ( HasAPIKey, )

    def get(self, request, format=None):
        serializer = PriceSerializer(BTCPrice.objects.all(), many=True)
        return Response({
                    "data": serializer.data,
                }, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        # api_url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={api_key}'
        try:
            api_url_key = api_url + api_key
            raw = requests.get(api_url_key).json()
            BTC_price = raw["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
            # BTC_price = 45.0393
            price = BTCPrice(price=BTC_price)
            price.save()
            price = PriceSerializer(price).data
            return Response({
                    "data": price,
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"message": "Price could not be received."},
                status=status.HTTP_408_REQUEST_TIMEOUT)