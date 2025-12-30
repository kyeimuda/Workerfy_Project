from django.urls import path
from .views import health_check, Tradespeople, TradeSpecialty_view, City_view, Country_view, jobs_view
from rest_framework import routers


urlpatterns = [
    path("health/", health_check, name='health_check'),
    path("tradespeople/", Tradespeople, name='tradespeople'),
    path("trade-specialty/", TradeSpecialty_view, name='trade_specialty'),
    path("countries/", Country_view, name='countries'),
    path("city/", City_view, name='city'),
    path("jobs/", jobs_view, name='jobs')
    ]