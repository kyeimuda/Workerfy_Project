import json

from rest_framework import serializers
from MainWorkerfy.models import JobPostAttachment, TradespersonProfile, City, Area, Country, Region, TradeSpecialty, TradeCategory\
    , TradeSkillTag, JobPost, Notification
from django.contrib.auth.models import User


# This is a serializer for the user model
class usersListSerializerl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']

class usersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],  # Assuming email is used as username
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user 


# Serializers for the TradeSkillTag model
class skillsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeSkillTag
        fields = '__all__'

# Serializers for the TradeSpecialty model
class TradeSpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeSpecialty
        fields = '__all__'



# Below are serializers for the tradesperson profile
class TradespeopleListSerializer(serializers.ModelSerializer):

    # trade_category = serializers.StringRelatedField()
    # trade_specialties = serializers.StringRelatedField()
    # base_location = serializers.StringRelatedField()
    # sub_location = serializers.StringRelatedField()
    skills = skillsTagSerializer(many=True, read_only=True)
    trade_specialties = TradeSpecialtySerializer(many=True, read_only=True)

    class Meta:
        model = TradespersonProfile
        fields = '__all__'


class TradespeopleWriteSerializer(serializers.ModelSerializer):

    skills = serializers.CharField(required=False)
    trade_specialties = serializers.CharField(required=False)

    class Meta:
        model = TradespersonProfile
        fields = '__all__'

    def _safe_capitalize(self, value):
        """Normalize a string value to a consistent capitalized form."""
        return value.capitalize() if isinstance(value, str) and value else value

    def _normalize_validated_data(self, validated_data):
        """Apply safe capitalization to string fields in validated_data."""
        for key, value in list(validated_data.items()):
            if isinstance(value, str):
                validated_data[key] = self._safe_capitalize(value.strip())
            elif isinstance(value, list):
                validated_data[key] = [self._safe_capitalize(v) for v in value]
        return validated_data

    def tradeSpecialtiesFields(self, validated_data):
        if "trade_specialties" in validated_data:
            specialityData = json.loads(validated_data["trade_specialties"])
            print(specialityData)
            validated_data.pop("trade_specialties")
            return specialityData
        return None

    def tradeSkillsFields(self, validated_data):
        if "skills" in validated_data:
            skillsData = json.loads(validated_data["skills"])
            print(skillsData)
            validated_data.pop("skills")
            return skillsData
        return None
            


    def create(self, validated_data):
        print(validated_data)
        validated_data = self._normalize_validated_data(validated_data)
        trade_specialties_data = self.tradeSpecialtiesFields(validated_data)
        skills_data = self.tradeSkillsFields(validated_data)

        tradesperson_profile = TradespersonProfile.objects.create(**validated_data)

        # Handle ManyToMany relationships
        if trade_specialties_data is not None:
            for specialty in trade_specialties_data:
                specialty_obj, created = TradeSpecialty.objects.get_or_create(category=tradesperson_profile.trade_category, name=specialty)
                tradesperson_profile.trade_specialties.add(specialty_obj)
        
        if skills_data is not None:
            for skill in skills_data:
                skill_obj, created = TradeSkillTag.objects.get_or_create(category=tradesperson_profile.trade_category, name=skill)
                tradesperson_profile.skills.add(skill_obj)



        return tradesperson_profile

    def update(self, instance, validated_data):
        print(validated_data)
        validated_data = self._normalize_validated_data(validated_data)
        trade_specialties_data = self.tradeSpecialtiesFields(validated_data)
        skills_data = self.tradeSkillsFields(validated_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if trade_specialties_data is not None:
            instance.trade_specialties.clear()
            for specialty in trade_specialties_data:
                specialty_obj, created = TradeSpecialty.objects.get_or_create(category=instance.trade_category, name=specialty)
                instance.trade_specialties.add(specialty_obj)

        if skills_data is not None:
            instance.skills.clear()
            for skill in skills_data:
                skill_obj, created = TradeSkillTag.objects.get_or_create(category=instance.trade_category, name=skill)
                instance.skills.add(skill_obj)

        if "other_skills" in validated_data and not None:
            perv_other_skills = instance.other_skills if instance.other_skills else []
            new_other_skills = validated_data["other_skills"]
            for skill in new_other_skills:
                if skill not in perv_other_skills:
                    perv_other_skills.append(skill)
            instance.other_skills = perv_other_skills
        instance.save()


        return instance


class NotificationListCreateUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
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



class jobattachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostAttachment
        fields = ['file', 'uploaded_at']

class jobsSerializer(serializers.ModelSerializer):
    attachments = jobattachmentsSerializer(many=True, read_only=True)
    user = usersCreateSerializer(read_only=True)
    

    class Meta:
        model = JobPost
        fields = '__all__'