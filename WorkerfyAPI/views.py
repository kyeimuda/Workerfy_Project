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

@api_view(['GET','PUT'])
def Tradespeople(request):
    """
    API for retrieving all tradespeople profiles.
    """
    try:
        Tradespeople = TradespersonProfile.objects.all()
        serialized_data = TradespeopleSerializer(Tradespeople)
    except Exception as error:
        return Response(api_response(success=False, message=f"{error}"), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(api_response(success=True, message="Tradespeople profiles retrieved successfully", data=serialized_data.data), status=status.HTTP_200_OK)


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