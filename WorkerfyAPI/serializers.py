from rest_framework import serializers
from MainWorkerfy.models import JobPostAttachment, TradespersonProfile, City, Area, Country, Region, TradeSpecialty, TradeCategory\
    , TradeSkillTag, JobPost
from django.contrib.auth.models import User


# This is a serializer for the user model
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'date_joined']

class TradespeopleListSerializer(serializers.ModelSerializer):
    trade_category = serializers.StringRelatedField()
    sub_location = serializers.StringRelatedField()
    skills = serializers.StringRelatedField(many=True)

    
    class Meta:
        model = TradespersonProfile
        fields = ['id', 'first_name', 'last_name', 'other_names', 'trade_category', 'profile_picture', 'sub_location', 'skills','rate_charged', 'experience_years']

class TradespeopleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradespersonProfile
        fields ='__all__'



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class TradeSpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeSpecialty
        fields = '__all__'

class TradeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeCategory
        fields = '__all__'

class TradeSkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeSkillTag
        fields = '__all__'

class jobattachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostAttachment
        fields = ['file', 'uploaded_at']

class jobsSerializer(serializers.ModelSerializer):
    attachments = jobattachmentsSerializer(many=True, read_only=True)
    user = userSerializer(read_only=True)
    

    class Meta:
        model = JobPost
        fields = '__all__'