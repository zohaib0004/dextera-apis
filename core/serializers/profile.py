from rest_framework import serializers
from ..models.profile import Profile, Group
from django.contrib.auth import get_user_model
 
User = get_user_model()

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =  ('id',
                    'first_name',
                    'middle_name',
                    'last_name',
                    'p_email',
                    'home',
                    'mobile',
                    'street',
                    'suite',
                    'city',
                    'state',
                    'zip',
                    'ext',
                   )

class ProfileShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =  ('id',
                    'user',
                    'first_name',
                    'last_name',
                    'role',
                    'c_email',
                   )


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Profile
        fields =  ('id',
                    'username',
                    'c_email',
                    'mobile',
                    'home',
                    'state',
                    'city',
                    'language',
                    'locate',
                    'search_active',
                    'law_school',
                    'grad_year',
                    'bar_admit_date',
                    'undergrad_school',
                    'undergrad_area',
                    'undergrad_year',
                    'bar_no',
                    'admitted_practice',
                    'practice_time',
                    'longest_tenure',
                    'average_tenure',
                    'current_tenure',
                    'past_bar_companies_no',
                    'primary_area',)

# Create new Member serializer 
class CreateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = (
            "id", 
            "first_name",
            "middle_name",
            "last_name",
            "p_email",
            "role",
            "c_email",
            "rate",
            "time_zone",
            "group",
            "job_title",
            "bar_no",
            "street",
            "suite",
            "city",
            "state",
            "zip",
            "ext",
            "mobile",
            "home",
            "work_no",
            "phone_ext",
        )

# Member serializers
class MembersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    last_login = serializers.CharField(source='user.last_login', read_only=True)
    is_active = serializers.CharField(source='user.is_active', read_only=True)
    class Meta:
        model = Profile
        fields =  (
            "id",
            'username',
            "last_login",
            "is_active",
            "first_name",
            "middle_name",
            "last_name",
            "p_email",
            "role",
            "c_email",
            "rate",
            "time_zone",
            "group",
            "job_title",
            "bar_no",
            "street",
            "suite",
            "city",
            "state",
            "zip",
            "ext",
            "mobile",
            "home",
            "work_no",
            "phone_ext",
        )
        def create(self, validated_data):
            username = validated_data['f_name'] + validated_data['l_name']
            password = validated_data['f_name'] + validated_data['l_name'] +"1234"
            user = User.objects.create_client(username, validated_data['f_name'],validated_data['l_name'], validated_data['p_email'],password)
            user.set_password(password)
            user.save()
            
            member = Profile.objects.create(validated_data)
            return member

# Group serializer
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields =  (
            "id",
            "name"
        )