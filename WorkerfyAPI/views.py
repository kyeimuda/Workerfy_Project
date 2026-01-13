from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from MainWorkerfy.models import JobPostAttachment, TradespersonProfile, City, Area, Country, Region, TradeSpecialty, TradeCategory, TradeSkillTag\
    , JobPost
from .serializers import CitySerializer, TradespeopleSerializer, TradeSpecialtySerializer, TradeCategorySerializer, TradeSkillTagSerializer\
    , CountrySerializer, jobattachmentsSerializer, jobsSerializer, userSerializer
from .API_format import api_response


@api_view(['GET', 'PUT'])
def user_view(request):
    """
    API for retrieving all users
    """
    users = User.objects.all()
    serialized_data = userSerializer(users, many=True)
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

@api_view(['GET'])
def jobattachments_view(request):
    """
    API for retrieving all job post attachments.
    """
    Attachments = JobPostAttachment.objects.all()
    serialized_data = jobattachmentsSerializer(Attachments, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def skills_view(request):
    try:
        skills = TradeSkillTag.objects.all()
        serialized_data = TradeSkillTagSerializer(skills, many=True)
    except Exception as error:
        return Response(api_response(success=False, message=f"{error}"))
    return Response(api_response(success=True, message="Successful", data=serialized_data.data))


@api_view(['GET', 'PUT'])
def Tradespeople_view(request):

    try:
        tradespeople = TradespersonProfile.objects.prefetch_related(
            'trade_category',
            'sub_location',
            'sub_location__region',
            'sub_location__region__country',
            'skills'
            ).all()
        serialized_data = TradespeopleSerializer(tradespeople, many=True, context={'request': request})
    except Exception as error:
        return Response(api_response(success=False, message=f"{error}", errors='HTTP_500_INTERNAL_SERVER_ERROR'), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(api_response(success=True, message="Successful", data=serialized_data.data))