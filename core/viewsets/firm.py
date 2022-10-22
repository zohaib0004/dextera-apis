# Create your views here.
from ..models.firm import BillingAddress, Firm, PaymentInfo
from rest_framework import  viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from ..serializers.firm import CreateFirmAccountSerializer, GetFirmAccountSerializer, CreateFirmAccountSerializer,PaymentInfoSerializer,BillingAddressSerializer,GetPaymentInfoSerializer,GetBillingAddressSerializer, UploadFirmLogo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import get_user_model

User = get_user_model()

class UploadFirmLogoViewset(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UploadFirmLogo
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Firm.objects.all()
        serializer = UploadFirmLogo(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = UploadFirmLogo(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UploadFirmLogoViewset(viewsets.ModelViewSet):
#     queryset = FirmLogo.objects.all()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = UploadFirmLogo

  
class GetFirmDetailViewSet(viewsets.ReadOnlyModelViewSet):
   
    queryset = Firm.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GetFirmAccountSerializer


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Firm.objects.all()
        user = self.request.query_params.get('user')
        
        if user is not None:
            queryset = Firm.objects.filter(owner=user )
        return queryset

    # def get_object(self):
    #     pk = self.kwargs.get('pk')

    #     if pk == "current":
    #         return self.request.user

    #     return super(GetFirmDetailViewSet, self).get_object()

class GetFirmSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Firm.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GetFirmAccountSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super(GetFirmAccountSerializer, self).get_object()


# class CreateFirmAccountViewSet(viewsets.ModelViewSet):
#     queryset = Firm.objects.all()
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = CreateFirmAccountSerializer
#     parser_classes = [MultiPartParser, FormParser]
    
#     # def retrieve(self, request, pk=None):
#     #     queryset = Profile.objects.get(username=pk)
#     #     profile = get_object_or_404(queryset, pk=1)
#     #     serializer = ProfileSerializer(profile)
#     #     return Response(serializer.data)
    
#     def create(self, request, format=None):
#         user = User.objects.get(id = self.request.user.id)
#         serializer = CreateFirmAccountSerializer(user= user, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_200_OK )
#         else:
#             return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class FirmAccountViewset(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = CreateFirmAccountSerializer
    permission_classes = [permissions.AllowAny]


class GetFirmAccountViewset(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = GetFirmAccountSerializer
    permission_classes = [permissions.AllowAny]


class PaymentInfoViewset(viewsets.ModelViewSet):
    queryset = PaymentInfo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentInfoSerializer


class BillingAddressViewset(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BillingAddressSerializer

class GetPaymentInfoViewset(viewsets.ModelViewSet):
    queryset = PaymentInfo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GetPaymentInfoSerializer


class GetBillingAddressViewset(viewsets.ModelViewSet):
    queryset = BillingAddress.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GetBillingAddressSerializer