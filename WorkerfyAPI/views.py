from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from MainWorkerfy.models import JobPostAttachment, TradespersonProfile, City, Area, Country, Region, TradeSpecialty, TradeCategory, TradeSkillTag\
    , JobPost
from .serializers import CitySerializer, TradespeopleListSerializer, TradeSpecialtySerializer, TradeCategorySerializer,\
      CountrySerializer, jobattachmentsSerializer, jobsSerializer, usersCreateSerializer, usersListSerializerl, skillsTagSerializer,\
     TradeSpecialtySerializer, TradespeopleWriteSerializer
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

""" @api_view(['GET'])
def TradeSpecialty_view(request):
    TradeSpecialties = TradeSpecialty.objects.all()
    serialized_data = TradeSpecialtySerializer(TradeSpecialties, many=True)
    return Response(serialized_data.data) """

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

""" @api_view(['GET'])
def skills_view(request):
    try:
        skills = TradeSkillTag.objects.all()
        serialized_data = TradeSkillTagSerializer(skills, many=True)
    except Exception as error:
        return Response(api_response(success=False, message=f"{error}"))
    return Response(api_response(success=True, message="Successful", data=serialized_data.data))
 """

@api_view(['GET', 'PUT'])
@permission_classes([])
def Tradespeople_view(request):

    try:
        tradespeople = TradespersonProfile.objects.prefetch_related(
            'trade_category',
            'sub_location',
            'sub_location__region',
            'sub_location__region__country',
            'skills'
            ).all()
        serialized_data = TradespeopleListSerializer(tradespeople, many=True, context={'request': request})
    except Exception as error:
        return Response(api_response(success=False, message=f"{error}", errors='HTTP_500_INTERNAL_SERVER_ERROR'), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(api_response(success=True, message="Successful", data=serialized_data.data))

class usersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related().all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return usersCreateSerializer
        if self.action in  ['list', 'retrieve']:
            return usersListSerializerl
        return usersListSerializerl



class TradespeopleViewSet(viewsets.ModelViewSet):
    queryset = TradespersonProfile.objects.prefetch_related(
            'trade_category',
            'sub_location',
            'sub_location__region',
            'sub_location__region__country',
            'skills'
            ).all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TradespeopleWriteSerializer
        return TradespeopleListSerializer


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        # Serialize with read serializer for the response
        read_serializer = TradespeopleListSerializer(instance, context=self.get_serializer_context())
        return Response(read_serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Serialize with read serializer for the response
        read_serializer = TradespeopleListSerializer(serializer.instance, context=self.get_serializer_context())
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_update(self, serializer):
        print(self.request.data)
        serializer.save()
    


class skillsTagViewSet(viewsets.ModelViewSet):
    queryset = TradeSkillTag.objects.all()
    serializer_class = skillsTagSerializer
    permission_classes = [IsAuthenticated]

class TradeSpecialtyViewSet(viewsets.ModelViewSet):
    queryset = TradeSpecialty.objects.all()
    serializer_class = TradeSpecialtySerializer
    permission_classes = [IsAuthenticated]
    

