from urllib import request
from accounts.models  import FunctionPermissions, Role, RoleCategory, RoleFunctions,  UserRole, Permissions
from rest_framework import status
from accounts.serializer.role import RoleFunctionsSerializer,FunctionPermissionsSerializer,RoleCategorySerializer,RoleCategoriesSerializer, GroupsSerializer, UserRoleSerializer, RoleFunctionssSerializers,RoleSerializer,RolesSerializer, RolePermissionFunctionSerializer,PermissionsSerializer,RolePermissionsSerializer
from rest_framework import generics, permissions,viewsets 
from accounts.models import Role,  UserRole, Permissions, Group
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from rest_framework import  viewsets, permissions
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


DOMAIN_LIST = ['gmail.com', 'yahoo.com',  'yahoo.com', 'live.com', 'outlook.com', 'hotmail.com', 'aol.com']

PERMISSIONS = ['Contact', 'Matter', 'Calender', 'Flat Fee', 'Expenses','Trust','Task(s)',
    'Invoice', 'Payments','Full DOB','Full SSN', 'Partial DOB', 'Partial SSN',
    'Roles', 'Reports', 'Discounts', 'Bank Acounts']
PERMISSIONS_ALL = ['view','edit', 'create', 'delete' ]

PERMISSIONS_CONTACT =['contacts', 'team', 'office', 'region']

FUNCTIONS = ['Contact', 
            'Matter', 
            'Calender', 
            'Flat Fee', 
            'Expenses',
            'Trust',
            'Task(s)',
            'Invoice', 
            'Payments',
            'Full DOB',
            'Full SSN', 
            'Partial DOB', 
            'Partial SSN',
            'Roles', 
            'Reports', 
            'Discounts', 
            'Bank Acounts']


@method_decorator(csrf_exempt, name='dispatch')
class ListPermissionsView(generics.ListAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UpdatePermissionView(generics.RetrieveUpdateAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ListRolesView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RolePermissionsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class GetRoleView(generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RolePermissionsSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UpdateRoleView(generics.RetrieveUpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RolePermissionsSerializer


# retrive all category 
class RoleCategoryViewset(generics.RetrieveAPIView):
    queryset = RoleCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoleCategorySerializer

class RoleCategoriesViewset(viewsets.ModelViewSet):
    queryset = RoleCategory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoleCategoriesSerializer

class RoleFunctionsViewset(viewsets.ModelViewSet):
  queryset = RoleFunctions.objects.all()
  permission_classes = [
        permissions.AllowAny
    ]
  
  serializer_class = RoleFunctionssSerializers



class RolesCreateView(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RolesSerializer

    def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      new_role = serializer.save()

      for item in FUNCTIONS:            
            func= RoleFunctions.objects.create(name = item, role=new_role)
            func.save()
            for perm in PERMISSIONS_ALL:
                permission= FunctionPermissions.objects.create(role = new_role, func = func, name = perm)
                permission.save()
            if item == "Contact":
                for c_perm in PERMISSIONS_CONTACT:
                    c_permission, create = FunctionPermissions.objects.get_or_create(role = new_role, func = func, name = c_perm)
                          
      return Response({
        "role": RolesSerializer(new_role, context=self.get_serializer_context()).data,
        "status": status.HTTP_200_OK
      })

class RolesCreate(viewsets.ModelViewSet):

  queryset = Role.objects.all()
  permission_classes = [
        permissions.AllowAny
    ]
  serializer_class = RolesSerializer


  def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      role = serializer.save()
      for item in FUNCTIONS:
          obj_fun = RoleFunctions.objects.create(role = role, name = item)
          obj_fun.save()          
          for perm in PERMISSIONS_ALL:
              obj_perm = FunctionPermissions.objects.create(role = role, func = obj_fun, name = perm)
              obj_perm.save()
          if item == "Contact":
              for c_perm in PERMISSIONS_CONTACT:
                  c_fun = FunctionPermissions.objects.create(role = role, func = obj_fun, name = c_perm)
                  c_fun.save()
      return Response({
        "role": RolesSerializer(role, context=self.get_serializer_context()).data,
        "status": status.HTTP_200_OK
      })

class RolesListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class SingleRoleView(generics.RetrieveUpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class DeleteRoleView(generics.DestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# class RolesCreateView(generics.CreateAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer

#     def create(self, request, *args, **kwargs):
#       serializer = self.get_serializer(data=request.data)
#       serializer.is_valid(raise_exception=True)
#       role = serializer.save()
#       for permission in PERMISSIONS:
#         fun = RoleFunctions.objects.create(role = role, name = permission)
#         fun.save()
#         permission = F

#       return Response({
#         "role": RoleSerializer(role, context=self.get_serializer_context()).data,
        
#         "status": status.HTTP_200_OK
#       })

class RoleFunctionsCreateView(generics.CreateAPIView):
    queryset = RoleFunctions.objects.all()
    serializer_class = RolePermissionFunctionSerializer

class RoleFunctionsListView(generics.ListAPIView):
    queryset = RoleFunctions.objects.all()
    serializer_class = RolePermissionFunctionSerializer

class SingleRoleFunctionView(generics.RetrieveUpdateAPIView):
    queryset = RoleFunctions.objects.all()
    serializer_class = RoleFunctionsSerializer

class DeleteRoleFunctionView(generics.DestroyAPIView):
    queryset = RoleFunctions.objects.all()
    serializer_class = RolePermissionFunctionSerializer


class RoleFunctionPermissionCreateView(generics.CreateAPIView):
  queryset = FunctionPermissions.objects.all()
  serializer_class = FunctionPermissionsSerializer

class RoleFunctionPermissionsListView(generics.ListAPIView):
  queryset = FunctionPermissions.objects.all()
  serializer_class = FunctionPermissionsSerializer

class DeleteRoleFunctionPermissionView(generics.DestroyAPIView):
  queryset = FunctionPermissions.objects.all()
  serializer_class = FunctionPermissionsSerializer

class SingleRoleFunctionPermissionView(generics.RetrieveUpdateAPIView):
  queryset = FunctionPermissions.objects.all()
  serializer_class = FunctionPermissionsSerializer


class RoleAPI(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('pk')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      role = serializer.save()
      for permission in PERMISSIONS:
        obj = Permissions.objects.create(role = role, name = permission)
        obj.save()
      return Response({
        "role": RoleSerializer(role, context=self.get_serializer_context()).data,
        
        "status": status.HTTP_200_OK
      })

class PermissionsAPI(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PermissionsSerializer


class UserRoleAPI(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserRoleSerializer

class RolePermissionAPI(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('pk')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RolePermissionsSerializer
    # lookup_field = 'role'

class GroupAPI(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupsSerializer


class RoleCategoryFunctionViewset(viewsets.ModelViewSet):
    queryset = RoleFunctions.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoleFunctionssSerializers

    
class RoleCategoryFilterViewset(viewsets.ModelViewSet):
    queryset = RoleFunctions.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoleFunctionssSerializers
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = RoleFunctions.objects.all()
        cat_id = self.request.query_params.get('cat_id')
        role_id = self.request.query_params.get('role_id')
        if cat_id is not None:
            queryset = RoleFunctions.objects.filter(category=cat_id, role=role_id )
        return queryset