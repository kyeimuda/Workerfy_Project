from django.urls import path
from .views import Tradespeople_view, City_view, Country_view, TradespeopleViewSet, jobattachments_view,\
      jobs_view, user_view, usersViewSet, skillsTagViewSet, TradeSpecialtyViewSet, NotificationsViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path("users/", user_view, name='users'),
    # path("tradespeople/", Tradespeople_view, name='tradespeople'),
  # path("trade-specialty/", TradeSpecialty_view, name='trade_specialty'),
    path("countries/", Country_view, name='countries'),
    path("city/", City_view, name='city'),
    path("job-attachments/", jobattachments_view, name='job_attachments'),
    path("jobs/", jobs_view, name='jobs'),
   #path("skills/", skills_view, name='skills')
    ]


router = DefaultRouter()
router.register(r'tradespeople', TradespeopleViewSet, basename='tradespeople')
router.register(r'users', usersViewSet, basename='users')
router.register(r'skills', skillsTagViewSet, basename='skills')
router.register(r'trade-specialties', TradeSpecialtyViewSet, basename='trade-specialties') 
router.register(r'notifications', NotificationsViewSet, basename='notifications')
urlpatterns += router.urls