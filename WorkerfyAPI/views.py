from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from MainWorkerfy.models import TradespersonProfile, City, Area, Country, Region, TradeSpecialty, TradeCategory, TradeSkillTag\
    , JobPost
from .serializers import CitySerializer, TradespeopleSerializer, TradeSpecialtySerializer, TradeCategorySerializer, TradeSkillTagSerializer\
    , CountrySerializer, jobsSerializer

@api_view(['GET'])
def health_check(request):
    """
    A simple health check endpoint to verify that the API is running.
    """
    data = []
    api = {}

    users = User.objects.all()

    for user in users:
        individual_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
        data.append(individual_data)

    api['data'] = data


    return Response(api, status=status.HTTP_200_OK)

@api_view(['GET'])
def Tradespeople(request):
    """
    API for retrieving all tradespeople profiles.
    """
    Tradespeople = TradespersonProfile.objects.all()
    serialized_data = TradespeopleSerializer(Tradespeople, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def City_view(request):
    """
    API for retrieving all cities.
    """
    Cities = City.objects.all()
    serialized_data = CitySerializer(Cities, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def TradeSpecialty_view(request):
    """
    API for retrieving all trade specialties.
    """
    TradeSpecialties = TradeSpecialty.objects.all()
    serialized_data = TradeSpecialtySerializer(TradeSpecialties, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def Country_view(request):
    """
    API for retrieving all countries for Workerfy.
    """
    Countries = Country.objects.all()
    serialized_data = CountrySerializer(Countries, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def jobs_view(request):
    """
    API for retrieving all job posts.
    """
    Jobs = JobPost.objects.all()
    serialized_data = jobsSerializer(Jobs, many=True)
    return Response(serialized_data.data)