# from ..models.address import State,County,City,ZipCode
# from rest_framework import viewsets, permissions
# from ..serializers.address import StateSerializer, CountySerializer, CitySerializer, ZipCodeSerializer


# class StateViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = State.objects.all()
#     permission_classes=[ permissions.AllowAny]
#     serializer_class= StateSerializer

# class SelectStateViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = State.objects.all()
#     permission_classes=[ permissions.AllowAny]
#     serializer_class= StateSerializer

# class CountyViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = County.objects.all()
#     permission_classes=[ permissions.AllowAny]
#     serializer_class= CountySerializer

# # select county and get full list of zipcode in it 
# class SelectCountyViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = ZipCode.objects.all()
#     permission_classes=[ permissions.AllowAny]
#     serializer_class= ZipCodeSerializer

#     # def retrieve(self, request, pk=None):

#     #     queryset = ZipCode.objects.get(county=pk)
#     #     profile = get_object_or_404(queryset, pk=1)
#     #     serializer = ZipCodeSerializer(profile)
#     #     return Response(serializer.data)

# class CityViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = City.objects.all()
#     permission_classes=[ permissions.AllowAny]
#     serializer_class= CitySerializer

# # class CityViewset(viewsets.ReadOnlyModelViewSet):
# #     queryset = City.objects.all()
# #     permission_classes=[ permissions.AllowAny]
# #     serializer_class= CitySerializer


# class ZipCodeViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = ZipCode.objects.all()
#     permission_classes=[ permissions.AllowAny]
#     serializer_class= ZipCodeSerializer