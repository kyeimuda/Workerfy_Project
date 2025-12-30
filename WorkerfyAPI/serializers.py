from rest_framework import serializers
from MainWorkerfy.models import TradespersonProfile, City, Area, Country, Region, TradeSpecialty, TradeCategory\
    , TradeSkillTag, JobPost


class TradespeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradespersonProfile
        fields = '__all__'

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

class jobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'