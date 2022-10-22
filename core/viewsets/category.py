from rest_framework import  viewsets, permissions
from ..serializers.category import CategorySerializer,SubCategorySerializer,ClassificationSerializer

from ..models.category import Category, SubCategory, Classification



class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer

class SubCategoryViewset(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubCategorySerializer

class ClassificationViewset(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClassificationSerializer