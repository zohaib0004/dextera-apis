from rest_framework import serializers
from django.contrib.auth import authenticate
from core.models.finance import FinanceAccount
from core.serializers.profile import CreateMemberSerializer, ProfileShortSerializer
from core.serializers.firm import GetFirmAccountSerializer, GetPaymentInfoSerializer,GetBillingAddressSerializer, UploadFirmLogo
from core.models.firm import Firm, PaymentInfo,BillingAddress
from core.models.profile import  Profile
from accounts.models import Group

from core.models.profile import Profile

from django.contrib.auth import get_user_model

User = get_user_model()

PERMISSIONS = ['Contact', 'Matter', 'Calender', 'Flat Fee', 'Expenses','Trust','Task(s)',
    'Invoice', 'Payments','Full DOB','Full SSN', 'Partial DOB', 'Partial SSN',
    'Roles', 'Reports', 'Discounts', 'Bank Acounts']

class UserSerializer(serializers.ModelSerializer):
  profile = ProfileShortSerializer(many=False)
  firm = GetFirmAccountSerializer(many=False)
  paymentInfo = GetPaymentInfoSerializer(many=False)
  billingAddress = GetBillingAddressSerializer(many=False)

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'is_superuser', 'is_firm', 'is_firm_employee', 'is_client', 'last_login', 'is_active', "profile", 'firm', 'paymentInfo','billingAddress')


class CreateUserSerializer(serializers.ModelSerializer):
  member = CreateMemberSerializer(many=False)
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name','last_name', 'email', 'password', "member")
  def create(self, validated_data):
        member_data = validated_data.pop('member')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **member_data)
        return user



class UserListSerializer(serializers.ModelSerializer):
  # member = serializers.RelatedField(read_only=True)
  class Meta:
    model = User
    fields = ('id', 'first_name','last_name',  'email', 'is_client', 'is_firm_employee', 'last_login', 'is_active')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id',  'username', 'first_name', 'last_name', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):    
    user = User.objects.create_firm(validated_data['username'], validated_data['first_name'],validated_data['last_name'], validated_data['email'], validated_data['password'])
    
    obj1, create = PaymentInfo.objects.get_or_create(user = user)
    obj1.save()
    obj2, create = BillingAddress.objects.get_or_create(user = user)
    obj2.save()
    firm, create = Firm.objects.get_or_create(owner = user)
    firm.save()
    finance, create = FinanceAccount.objects.get_or_create(owner = user)
    finance.save()
    profile, create  = Profile.objects.get_or_create(user = user, first_name= validated_data['first_name'],last_name =validated_data['last_name'], c_email=validated_data['email'])
    profile.save()    
    return user


class CreateFirmSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id',  'username', 'first_name', 'last_name',  'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_firm(validated_data['username'], validated_data['first_name'],validated_data['last_name'], validated_data['email'], validated_data['password'])
    group = "firm",
    role="Manager"
    finance, create = FinanceAccount.objects.get_or_create(owner = user)
    finance.save()
    member, create  = Profile.objects.get_or_create(user = user, first_name= validated_data['first_name'],last_name =validated_data['last_name'], email=validated_data['email'], role=role, group=group)
    member.save()

    return user

class CreateFirmEmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id',  'username', 'first_name', 'last_name',  'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_firm_employee(validated_data['username'], validated_data['first_name'],validated_data['last_name'], validated_data['email'], validated_data['password'])
    group = "firm",
    role="Jr. Atterney"
    finance, create = FinanceAccount.objects.get_or_create(owner = user)
    finance.save()
    member, create  = Profile.objects.get_or_create(user = user, first_name= validated_data['first_name'],last_name =validated_data['last_name'], email=validated_data['email'], role=role, group=group)
    member.save()

    return user

class CreateClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id',  'username', 'first_name', 'last_name',  'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_client(validated_data['username'], validated_data['first_name'],validated_data['last_name'], validated_data['email'], validated_data['password'])
    group = "client",
    role=""
    finance, create = FinanceAccount.objects.get_or_create(owner = user)
    finance.save()
    member,create  = Profile.objects.get_or_create(user = user, first_name= validated_data['first_name'],last_name =validated_data['last_name'], email=validated_data['email'], role=role, group=group)
    member.save()
    return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")

class IsActiveUser(serializers.ModelSerializer):
  class Meta:
    model= User
    fields = ['id', 'is_active']

