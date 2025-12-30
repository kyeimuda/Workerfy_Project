from django.urls import path
from . import views

urlpatterns = [
        path('forms', views.forms, name='forms'),
        path('Main', views.Main_page, name='MainPage'),
        path('EditTradesperson', views.TradespersonProfileEdit, name='MainTradespersonProfileEditnPage'),
        path('jobPost', views.job_Post_Page, name='jobPostPage'),
        path('jobPostDetails', views.jobPostDetailsPage, name="JobPostDetails"),
        path('Work', views.Work_Page, name='Work_Page'),
        path('Profile', views.Profile_Page, name='Profile_Page'),
        path('Discover', views.Discover_Page, name='Discover_Page'),
        path('Notifications', views.Notifications_Page, name='Notifications_Page'),
        path('More', views.More_Page, name='More_Page'),
    ]