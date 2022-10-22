from rest_framework import generics, permissions, viewsets
from rest_framework import status
from rest_framework.response import Response
from knox.models import AuthToken
from core.models.profile import Profile
from accounts.serializer.account import CreateUserSerializer, CreateFirmEmployeeSerializer, IsActiveUser,  UserListSerializer,CreateClientSerializer, UserSerializer, RegisterSerializer, LoginSerializer

from rest_framework import generics, permissions 
from rest_framework.views import APIView

from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework import  viewsets, permissions
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

DOMAIN_LIST = ['gmail.com', 'yahoo.com',  'yahoo.com', 'live.com', 'outlook.com', 'hotmail.com', 'aol.com']

PERMISSIONS = ['Contact', 'Matter', 'Calender', 'Flat Fee', 'Expenses','Trust','Task(s)',
    'Invoice', 'Payments','Full DOB','Full SSN', 'Partial DOB', 'Partial SSN',
    'Roles', 'Reports', 'Discounts', 'Bank Acounts']




# Registeration Api view for registering user 
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer
  def post(self, request, *args, **kwargs):
   
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # check for the domain is already exist if yes send the message 
    # "please contact in your comany to create your account."
    # else create account 
    if serializer.is_valid():
          # getting email from 
          email = serializer.validated_data['email']
          domain_name = email.split('@')[1]
          
          # first check if its a common domain or company domain 
          # checking for common email domain
          if domain_name in DOMAIN_LIST: 
            
            # raise error of not allow this domain. 
                return Response(serializer.errors,
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)
          # check if the domain is in the database 

          # one way to check
          # isDomain = User.objects.filter(domain = domain_name).count()
          
          # second way to check if the domain is already exists or not
          if User.objects.filter(domain = domain_name).exists():
            return Response(serializer.errors,
                        status=status.HTTP_409_CONFLICT)
          else:
            user = serializer.save()
            
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1],
                "status": status.HTTP_200_OK,
              })         
    else:
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
  
# Register client 
class CreateClientAPI(viewsets.ModelViewSet):
  serializer_class = CreateClientSerializer
  queryset = User.objects.all()

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    obj = Profile.objects.create(role = serializer.validated_data['role'], name = serializer.validated_data['permission'])
    obj.save()
    return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "status": status.HTTP_200_OK})

# registering firm employee 
class CreateFirmEmployeeAPI(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = CreateFirmEmployeeSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "status": status.HTTP_200_OK})

# login user 
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    _, token = AuthToken.objects.create(user)
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token,
      "status": status.HTTP_200_OK
    })

# for accessing user data 
class UserAPI(generics.RetrieveAPIView):
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user

class UserListAPI(viewsets.ModelViewSet):
  queryset = User.objects.all()
  permission_classes = [
        permissions.AllowAny
    ]
  serializer_class = UserListSerializer

class UserListFiveAPI(viewsets.ModelViewSet):
  # list of last 10 users 
  queryset = User.objects.all().order_by('-id')[:10]
  permission_classes = [
        permissions.AllowAny
    ]
  serializer_class = UserListSerializer

class CreateUserViewset(viewsets.ModelViewSet):
  queryset = User.objects.all()
  permission_classes =[permissions.AllowAny]
  serializer_class= CreateUserSerializer


class IsActiveUserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IsActiveUser



