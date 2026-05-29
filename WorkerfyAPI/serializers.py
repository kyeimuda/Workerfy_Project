import json

from rest_framework import serializers
from MainWorkerfy.models import JobPostAttachment, TradespersonProfile, City, Area, Country, Region, TradeSpecialty, TradeCategory,\
      TradeSkillTag, JobPost, Notification, ClientProfile, PortfolioItem
from django.contrib.auth import get_user_model

User = get_user_model()

# This is a serializer for the user model
class usersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'date_joined']

class usersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
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

    trade_category = serializers.StringRelatedField()
    # trade_specialties = serializers.StringRelatedField()
    # base_location = serializers.StringRelatedField()
    sub_location = serializers.StringRelatedField()
    skills = skillsTagSerializer(many=True, read_only=True)
    trade_specialties = TradeSpecialtySerializer(many=True, read_only=True)

    class Meta:
        model = TradespersonProfile
        fields = '__all__'

class TradespeopleSerializerAddedToJobs(serializers.ModelSerializer):
    trade_category = serializers.StringRelatedField()
    # trade_specialties = serializers.StringRelatedField()
    # base_location = serializers.StringRelatedField()
    sub_location = serializers.StringRelatedField()
    class Meta:
        model = TradespersonProfile
        fields = '__all__'


class TradespeopleWriteSerializer(serializers.ModelSerializer):

    skills = serializers.CharField(required=False)
    trade_specialties = serializers.CharField(required=False)
    delete_skill = serializers.CharField(required=False, write_only=True)
    delete_speciality = serializers.CharField(required=False, write_only=True)
    delete_other_skill = serializers.CharField(required=False, write_only=True)

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

    def _parse_id_list(self, value):
        if value is None or value == "":
            return []
        if isinstance(value, list):
            return [int(item) for item in value if str(item).strip().isdigit()]
        if isinstance(value, str):
            try:
                parsed = json.loads(value)
            except json.JSONDecodeError:
                parsed = [item.strip() for item in value.split(',') if item.strip()]
            if isinstance(parsed, list):
                ids = []
                for item in parsed:
                    if isinstance(item, int):
                        ids.append(item)
                    elif isinstance(item, str) and item.isdigit():
                        ids.append(int(item))
                return ids
        return []

    def tradeSpecialtiesFields(self, validated_data):
        if "trade_specialties" in validated_data:
            specialityData = json.loads(validated_data["trade_specialties"])
            validated_data.pop("trade_specialties")
            return specialityData
        return None

    def tradeSkillsFields(self, validated_data):
        if "skills" in validated_data:
            skillsData = json.loads(validated_data["skills"])
            validated_data.pop("skills")
            return skillsData
        return None

    def deleteSkillFields(self, validated_data):
        if "delete_skill" in validated_data:
            delete_ids = self._parse_id_list(validated_data.pop("delete_skill"))
            return delete_ids if delete_ids else None
        return None

    def deleteSpecialityFields(self, validated_data):
        if "delete_speciality" in validated_data:
            delete_ids = self._parse_id_list(validated_data.pop("delete_speciality"))
            return delete_ids if delete_ids else None
        return None

    def deleteOtherSkillsFields(self, validated_data):
        print(validated_data)
        if "delete_other_skill" in validated_data:
            raw_value = validated_data.pop("delete_other_skill")
            print(raw_value)
            try:
                parsed = json.loads(raw_value) if isinstance(raw_value, str) else raw_value
            except (json.JSONDecodeError, TypeError):
                parsed = [item.strip() for item in str(raw_value).split(',') if item.strip()]

            if isinstance(parsed, list):
                return [str(item).strip() for item in parsed if str(item).strip()]
        return None

    def create(self, validated_data):
        trade_specialties_data = self.tradeSpecialtiesFields(validated_data)
        skills_data = self.tradeSkillsFields(validated_data)
        delete_skill_ids = self.deleteSkillFields(validated_data)
        delete_speciality_ids = self.deleteSpecialityFields(validated_data)
        delete_other_skills = self.deleteOtherSkillsFields(validated_data)
        
        validated_data = self._normalize_validated_data(validated_data)
        
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

        # delete_skill is supported but there is no relation to detach on creation.
        return tradesperson_profile

    def update(self, instance, validated_data):
        trade_specialties_data = self.tradeSpecialtiesFields(validated_data)
        skills_data = self.tradeSkillsFields(validated_data)
        delete_skill_ids = self.deleteSkillFields(validated_data)
        delete_speciality_ids = self.deleteSpecialityFields(validated_data)
        delete_other_skills = self.deleteOtherSkillsFields(validated_data)
        
        validated_data = self._normalize_validated_data(validated_data)

        if trade_specialties_data is not None:
            for specialty in trade_specialties_data:
                specialty_obj, created = TradeSpecialty.objects.get_or_create(category=instance.trade_category, name=specialty)
                instance.trade_specialties.add(specialty_obj)

        if skills_data is not None:
            instance.skills.clear()
            for skill in skills_data:
                skill_obj, created = TradeSkillTag.objects.get_or_create(category=instance.trade_category, name=skill)
                instance.skills.add(skill_obj)

        if delete_skill_ids is not None:

            try:
                skills = TradeSkillTag.objects.filter(id__in=delete_skill_ids)
                for skill in skills:
                    instance.skills.remove(skill)
            except TradeSkillTag.DoesNotExist:
                return f"Some skills to delete were not found."

        if delete_speciality_ids is not None:
            try:
                specialities = TradeSpecialty.objects.filter(id__in=delete_speciality_ids)
                for speciality in specialities:
                    instance.trade_specialties.remove(speciality)
            except TradeSpecialty.DoesNotExist:
                return f"Some specialties to delete were not found."

        if delete_other_skills is not None:
            print( 'Deleting other skill', delete_other_skills)
            print(instance.other_skills)

            try:
                current_other_skills = instance.other_skills if instance.other_skills else []
                updated_other_skills = [skill for skill in current_other_skills if skill not in delete_other_skills]
                instance.other_skills = updated_other_skills
            except Exception as e:
                return f"An error occurred while deleting other skills: {str(e)}"

        if "other_skills" in validated_data and validated_data.get("other_skills") is not None:
            perv_other_skills = instance.other_skills if instance.other_skills else []
            new_other_skills = validated_data.pop("other_skills")
            if isinstance(new_other_skills, str):
                try:
                    new_other_skills = json.loads(new_other_skills)
                except json.JSONDecodeError:
                    new_other_skills = [item.strip() for item in new_other_skills.split(',') if item.strip()]
            for skill in new_other_skills:
                if skill not in perv_other_skills:
                    perv_other_skills.append(skill)
            instance.other_skills = perv_other_skills

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
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

class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'

class jobsSerializer(serializers.ModelSerializer):
    attachments = jobattachmentsSerializer(many=True, read_only=True)
    user = usersListSerializer(read_only=True)
    tradesperson = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()

    trade_category = serializers.StringRelatedField()
    # trade_specialties = serializers.StringRelatedField()
    # base_location = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = JobPost
        fields = '__all__'

    def get_tradesperson(self, obj):
        if obj.user.user_type == 'Tradesperson':
            try:
                profile = obj.user.tradesperson_profile
                return TradespeopleSerializerAddedToJobs(profile, context=self.context).data
            except TradespersonProfile.DoesNotExist:
                return None
        return None

    def get_client(self, obj):
        if obj.user.user_type == 'Client':
            try:
                profile = obj.user.client
                return ClientProfileSerializer(profile, context=self.context).data
            except ClientProfile.DoesNotExist:
                return None
        return None

class PortfolioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = '__all__'

    def create(self, validated_data):
        portfolio_item = PortfolioItem.objects.create(**validated_data)
        return portfolio_item