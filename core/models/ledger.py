from django.db import models


class LedgerTime(models.Model):

    contact= models.IntegerField(default=0, null=True)
    matter_name = models.IntegerField(default=0,null=True)
    category = models.CharField(max_length=255, null= True)
    sub_category = models.CharField(max_length=255, null= True)
    hard = models.BooleanField(default=False, null=True)
    soft = models.BooleanField(default=False, null=True)
    unit = models.IntegerField(default=0, null=True)
    qty = models.IntegerField(default=0, null=True)
    rate = models.IntegerField(default=0, null=True)
    file = models.CharField(max_length=500,default="", null=True)
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    detail = models.CharField(max_length=800, null= True)
    bill_by = models.IntegerField(default=0, null=True)
    billable = models.BooleanField(default=False, null=True)
    note = models.CharField(max_length=800, null= True)

  
    # timestemps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)