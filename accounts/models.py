from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.name

class UserAccountManager(BaseUserManager):
    def create_user(self,username, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.create(username=username, first_name= first_name, last_name=last_name, email=email)
        user.domain = email.split('@')[1]
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self,username, first_name, last_name, email, password):
        user = self.create_user(username, first_name, last_name, email, password)
        user.domain = email.split('@')[1]
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        
        user.save()

        return user

    def create_firm(self, username, first_name, last_name, email, password):
        user = self.create_user(username, first_name, last_name, email, password) 
        user.domain = email.split('@')[1]
        user.is_firm = True
        user.is_active = True
        user.save()

        return user


    def create_firm_employee(self, username, first_name, last_name, email, password):
        user = self.create_user(username, first_name, last_name, email, password) 
        user.domain = email.split('@')[1]
        user.is_firm_employee = True
        user.save()

        return user

    def create_client(self, username, first_name, last_name, email, password):
        user = self.create_user(username, first_name, last_name, email, password)
        user.domain = email.split('@')[1]
        user.is_client = True
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # owner of the firm 
    is_firm = models.BooleanField(default=False)
    # worker of the firm 
    is_firm_employee = models.BooleanField(default=False)
    # client of the firm 
    is_client = models.BooleanField(default = False)
    
    domain = models.CharField(max_length=100)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def get_full_name(self):
        return self.first_name + self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email

class Permissions(models.Model):
    role =  models.ForeignKey(Role, related_name="permissions", on_delete=models.CASCADE)
    role_category = models.CharField(max_length=255, null=True, blank= True)
    name = models.CharField(max_length=255)
    is_view = models.BooleanField(default=False)
    is_edit = models.BooleanField(default=False)
    is_create  = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_contacts = models.BooleanField(default=False)
    is_team = models.BooleanField(default=False)
    is_office = models.BooleanField(default=False)
    is_region  = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class RoleCategory(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['id']

class RoleFunctions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role_functions")
    category = models.ForeignKey(RoleCategory, on_delete=models.CASCADE, related_name="category_function")
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['id']
        # unique_together = ['role', 'name']
    
    def __str__(self):
        return self.name

class FunctionPermissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="role_function_permission", null=True, blank=True)
    func = models.ForeignKey(RoleFunctions, on_delete=models.CASCADE, related_name="function_permission", null=True, blank=True)
    name = models.CharField(max_length=50)
    is_set = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.ForeignKey(UserAccount, verbose_name="user", on_delete=models.CASCADE)
    role = models.ForeignKey(Role, verbose_name="role", on_delete=models.CASCADE)


