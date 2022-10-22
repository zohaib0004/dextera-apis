from dataclasses import field
from unicodedata import category
from rest_framework import serializers
from accounts.models import  FunctionPermissions, RoleCategory, RoleFunctions, Role,  UserRole, Permissions
from core.serializers.profile import CreateMemberSerializer
from django.contrib.auth.models import Group 
from django.contrib.auth import get_user_model

User = get_user_model()


class FunctionPermissionsSerializer(serializers.ModelSerializer):   
    class Meta:
        model= FunctionPermissions
        fields=(
            'id',
            'role',
            'func',
            'name',
            'is_set',
  
        )

        
class RoleFunctionsSerializer(serializers.ModelSerializer):
    function_permission = FunctionPermissionsSerializer(many=True)
    class Meta:
        model= RoleFunctions
        fields=(
            'id',
            "name",
            "role",
            'category',
            'function_permission',
            
        )
class RolePermissionFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model= FunctionPermissions
        fields=(
            'id',
            'role',
            'func',
            'name',
            'function_permission',
        )


class RoleSerializer(serializers.ModelSerializer):
    # role_functions = RoleFunctionsSerializer(many=True)
    class Meta:
        model = Role
        fields=(
            "id",
            "name"
        )
        

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields=(
            "id",
            "name",
        )

class RoleCategorySerializer(serializers.ModelSerializer):
    role_functions = RoleFunctionsSerializer(many=True)   
    class Meta:
        model= RoleCategory
        fields=(
            'id',
            'name',
            
            'role_functions',
        )


class RoleCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model= RoleCategory
        fields=(
            'id',
            'name',
        )
class RoleFunctionssSerializers(serializers.ModelSerializer):
    function_permission = FunctionPermissionsSerializer(many=True)
    class Meta:
        model = RoleFunctions
        fields =("id", "name", "role", "category", "function_permission" )

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields=(
            "id",
            "name"
        )
        
class PermissionsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Permissions
      fields = ('id', 'name', 'role', "is_view","is_edit","is_create","is_delete","is_contacts","is_team","is_office","is_region")

class UserRoleSerializer(serializers.ModelSerializer):
   class Meta:
      model = UserRole
      fields = ('user', 'role')




class RolePermissionsSerializer(serializers.ModelSerializer):
  permissions = PermissionsSerializer(many=True)
  class Meta:
      model = Role
      fields = ['id', 'name', 'permissions']


class GroupsSerializer(serializers.ModelSerializer):
  class Meta:
      model = Group
      fields = ['id', 'name']