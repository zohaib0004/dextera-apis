# from rest_framework import serializers
# from ..models.address import State, County, City, ZipCode

# class ZipCodeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= ZipCode
#         fields = ("id", "zip_code")


# class CitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model= City
#         fields = ("id", "name")

# class CountySerializer(serializers.ModelSerializer):
#     city = CitySerializer(many=True)
#     class Meta:
#         model= County
#         fields = ("id", "name", "state", "city" )


# class StateSerializer(serializers.ModelSerializer):
#     county = CountySerializer(many=True)
#     class Meta:
#         model= State
#         fields = ("id","name", "county")



