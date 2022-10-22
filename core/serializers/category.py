from rest_framework import serializers
from ..models.category import Category, SubCategory, Classification

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =  (
            "id",
            "name"
        )
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields =  (
            "id",
            "name"
        )
class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields =  (
            "id",
            "name"
        )