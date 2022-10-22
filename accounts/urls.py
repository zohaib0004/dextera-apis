from django.urls import path, include
from .viewset.account import UserListFiveAPI, CreateUserViewset, RegisterAPI, LoginAPI, UserAPI,CreateClientAPI, CreateFirmEmployeeAPI, UserListAPI, IsActiveUserAPI
from .viewset.role import  GroupAPI,ListPermissionsView,ListRolesView,GetRoleView,UpdateRoleView, UpdatePermissionView, PermissionsAPI, RolePermissionAPI, UserRoleAPI
from .viewset.role import DeleteRoleView, RolesCreate, RolesListView, RolesCreateView,RoleCategoryFunctionViewset, SingleRoleView,RoleFunctionsViewset,RoleCategoryViewset,RoleCategoriesViewset, RoleCategoryViewset
from .viewset.role import RoleFunctionsListView, RoleAPI, SingleRoleFunctionView, DeleteRoleFunctionView,RoleFunctionsCreateView
from .viewset.role import RoleCategoryFilterViewset, RoleFunctionPermissionCreateView,RoleFunctionPermissionsListView,DeleteRoleFunctionPermissionView,SingleRoleFunctionPermissionView
from knox import views as knox_views

from rest_framework import routers

router = routers.DefaultRouter()



router.register('auth/create-user-member',CreateUserViewset, "create-user-member"),
router.register('auth/users-list', UserListAPI, "users_list"),
router.register('auth/users-list-five', UserListFiveAPI, "users_list-five"),


# role permission urls 
router.register('auth/category-functions', RoleCategoryFunctionViewset, "category-functions"),
router.register('auth/role-functions', RoleFunctionsViewset, "role-functions"),
router.register('auth/roles', RoleAPI, "roles"),
router.register('auth/users-role-list', UserRoleAPI, "users_role_list"),
router.register('auth/permissions', PermissionsAPI, "permissions"),
router.register('auth/role-permissions', RolePermissionAPI, "role_permissions"),
router.register('auth/groups', GroupAPI, "group"),
router.register('auth/is-active-user', IsActiveUserAPI, "is_active_user"),
router.register('auth/register-client', CreateClientAPI, "register-client" ),
router.register('auth/register-firm-employee', CreateFirmEmployeeAPI, "register_firm_employe"),
router.register('role-create', RolesCreate, "role_create"),
router.register("role-cat-filter",  RoleCategoryFilterViewset, "role-cat-filter"),
router.register("auth/role-categories",RoleCategoriesViewset, "role-categories"),


urlpatterns = router.urls + [
# authentication related urls
  path('auth', include('knox.urls')),
  path('auth/register', RegisterAPI.as_view()),  
  path('auth/login', LoginAPI.as_view()),
  path('auth/user', UserAPI.as_view()),  
  path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),


# role permissions urls 
  path("auth/role-category/<int:pk>/",RoleCategoryViewset.as_view()),
  path('permissions-list/', ListPermissionsView.as_view()),
  path('permission-update/<int:pk>/', UpdatePermissionView.as_view()),
  path('roles-list/', ListRolesView.as_view()),
  path('role-update/<int:pk>/', GetRoleView.as_view()),
  path('role-get/<int:pk>/', UpdateRoleView.as_view()),
  
  path('role-create-view/', RolesCreateView.as_view()),

  path('role-single-view/<int:pk>/', SingleRoleView.as_view()),
  path('role-delete-view/<int:pk>/', DeleteRoleView.as_view()),

  path('role-list/', RolesListView.as_view()),
  

  path('role-function-create/', RoleFunctionsCreateView.as_view()),
  path('role-function-list/', RoleFunctionsListView.as_view()),
  path('role-function-delete/<int:pk>/',DeleteRoleFunctionView.as_view()),
  path('role-function-single/<int:pk>/',SingleRoleFunctionView.as_view()),

  path('role-function-permission-create/', RoleFunctionPermissionCreateView.as_view()),
  path('role-function-permissions-list/', RoleFunctionPermissionsListView.as_view()),
  path('role-function-permission-delete/<int:pk>/',DeleteRoleFunctionPermissionView.as_view()),
  path('role-function-permission-single/<int:pk>/',SingleRoleFunctionPermissionView.as_view()),
  
]

