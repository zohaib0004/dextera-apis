from django.db import models

# here we manage the matter and its tasks   

class Matter(models.Model):
    # matter_id = models.IntegerField(default=0) # used as a ref
    contact= models.IntegerField(default=0, null=True)
    matter_name = models.CharField(max_length=255,null=True)
    matter_type = models.CharField(max_length=255, null=True)
    matter_source = models.CharField(max_length=255, null=True)
    matter_status = models.CharField(max_length=255, null=True)
    assign_to = models.IntegerField(default=0, null=True) # ref to user only populated with lawyer
    assign_by = models.IntegerField(default=0, null=True) # ref to firm user
    billing_rate = models.FloatField(default=0.00, null=True)
    alerts = models.CharField(max_length=255, null=True)
    open_date = models.DateField(null=True)
    close_date = models.DateField(null=True)
    total_days =  models.IntegerField(default=0, null=True)

    jurisdiction= models.CharField(max_length=255, null=True)
    status_limitaion= models.CharField(max_length=255, null=True)
    opposing_counsel= models.CharField(max_length=255, null=True)
    where= models.CharField(max_length=255, null=True)
    when=  models.DateField(null=True)
    involved= models.CharField(max_length=255, null=True)
    witnesses= models.CharField(max_length=255, null=True)
    narrative= models.CharField(max_length=255, null=True)
    # timestemps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Task(models.Model):   
    matter_id = models.IntegerField(default=0, null=True)
    matter_contact = models.IntegerField(default=0, null=True)
    matter = models.CharField(max_length=255, default="", null=True)
    is_billable = models.BooleanField(default=False, null=True)
    is_private = models.BooleanField(default=False, null=True)  
    task  = models.CharField(max_length=255, null=True)
    last_action = models.DateField(null=True)
    next_action= models.DateField(null=True)
    detail = models.CharField(max_length=800, null=True)
    file = models.CharField(max_length=500,default="", null=True)
    assign_to = models.IntegerField(default=0,null=True)
    status = models.CharField(max_length=255,default="", null=True)
    task_nature = models.CharField( max_length=255, null=True)

    # timestemps
    due_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

