from django.urls import path
from .views import Tradespeople_view, TradeSpecialty_view, City_view, Country_view, jobattachments_view,\
      jobs_view, user_view, skills_view
from rest_framework import routers


urlpatterns = [
    path("users/", user_view, name='users'),
    path("tradespeople/", Tradespeople_view, name='tradespeople'),
    path("trade-specialty/", TradeSpecialty_view, name='trade_specialty'),
    path("countries/", Country_view, name='countries'),
    path("city/", City_view, name='city'),
    path("job-attachments/", jobattachments_view, name='job_attachments'),
    path("jobs/", jobs_view, name='jobs'),
    path("skills/", skills_view, name='skills')
    ]