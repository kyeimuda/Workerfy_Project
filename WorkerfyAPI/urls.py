from django.urls import path
from .views import Tradespeople, TradeSpecialty_view, City_view, Country_view, jobattachments_view,\
      jobs_view, user_view
from rest_framework import routers


urlpatterns = [
    path("users/", user_view, name='users'),
    path("tradespeople/", Tradespeople, name='tradespeople'),
    path("trade-specialty/", TradeSpecialty_view, name='trade_specialty'),
    path("countries/", Country_view, name='countries'),
    path("city/", City_view, name='city'),
    path("job-attachments/", jobattachments_view, name='job_attachments'),
    path("jobs/", jobs_view, name='jobs')
    ]