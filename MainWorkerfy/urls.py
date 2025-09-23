from django.urls import path
from . import views

urlpatterns = [
        path('forms', views.forms, name='forms'),
        path('Main', views.Main_page, name='MainPage'),
        path('EditTradesperson', views.TradespersonProfileEdit, name='MainTradespersonProfileEditnPage'),
    ]