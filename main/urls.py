from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import GetUsdRateView

# router = DefaultRouter()
# router.register('get-current-usd', GetUsdRateView, basename='get-current-usd')


urlpatterns = [
    path('get-current-usd/', GetUsdRateView.as_view()),
]