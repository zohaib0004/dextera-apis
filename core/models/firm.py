from django.db import models

from django.utils.translation import gettext_lazy as _
from accounts.models import UserAccount



def upload_to(instance, filename):
    return 'logos/{filename}'.format(filename=filename)

class Firm(models.Model):
    owner = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name="firm", blank=True, null=True)
    logo =  models.ImageField(upload_to="firm_logos", default= 'logos/default_logo.png', null=True, blank=True)
    c_name= models.CharField(max_length=255, null=True, blank=True, default="")
    dba_name= models.CharField(max_length=255, null=True, blank=True)
    tax_id= models.CharField(max_length=255, null=True, blank=True)
    tax_id_ext= models.CharField(max_length=255, null=True, blank=True)
    website= models.CharField(max_length=255, null=True, blank=True)
    office= models.CharField(max_length=255, null=True, blank=True)
    c_street= models.CharField(max_length=255, null=True, blank=True)
    c_suite= models.CharField(max_length=255, null=True, blank=True)
    c_city= models.CharField(max_length=255, null=True, blank=True)
    c_state= models.CharField(max_length=255, null=True, blank=True)
    c_zip= models.CharField(max_length=255, null=True, blank=True)
    c_ext= models.CharField(max_length=255, null=True, blank=True)
    is_created= models.BooleanField(default=False)
    # timestemps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FirmEmployee(models.Model):
    employee = models.ForeignKey(UserAccount, on_delete=models.CASCADE,related_name="firmEmployee")
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, related_name="firmEmployee")
    # timestemps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FirmClient(models.Model):
    Client = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="firmClient")
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, related_name="firmClient")
    # timestemps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class PaymentInfo(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name="paymentInfo", blank=True, null=True)
    # account details
    account_name = models.CharField(max_length=255, null=True, blank=True)
    account_no = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    rounting = models.CharField(max_length=255, null=True, blank=True)
    credit_card = models.CharField(max_length=255, null=True, blank=True)
    card_no =  models.CharField(max_length=255, null=True, blank=True)
    security_id = models.CharField(max_length=255, null=True, blank=True)
    expire_date = models.DateField( null=True, blank=True)
    is_created= models.BooleanField(default=False)

    # timestemps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BillingAddress(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name="billingAddress")
    # monthly or yearly 
    is_monthly = models.BooleanField(default=True)
    # plan 01 or plan 02
    plan = models.BooleanField(default=True)
    # address 
    street= models.CharField(max_length=255, null=True, blank=True)
    suite= models.CharField(max_length=255, null=True, blank=True)
    city= models.CharField(max_length=255, null=True, blank=True)
    state= models.CharField(max_length=255, null=True, blank=True)
    zip= models.CharField(max_length=255, null=True, blank=True)
    ext= models.CharField(max_length=255, null=True, blank=True)

    is_created= models.BooleanField(default=False)
    
    # timestemps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

