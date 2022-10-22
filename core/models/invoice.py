from django.db import models

class Invoice(models.Model):
    inv_client_id = models.IntegerField()
    inv_created_at = models.DateField(max_length=8)
    inv_payed_at = models.DateField(max_length=8)
    inv_client_name = models.CharField(max_length=50)
    inv_disputed = models.CharField(max_length=200)
    inv_due_at = models.DateField(max_length=8)
    inv_interest_due_at = models.DateField(max_length=8)
    inv_status = models.CharField(max_length=10)
    inv_matter_id = models.CharField(max_length=50) # ref to matter
    inv_note = models.TextField(max_length=500)
    inv_date_period = models.DateField(max_length=8)
    inv_term_contidion = models.TextField(max_length=1000)
    inv_void = models.CharField(max_length=200)
    inv_amount =models.FloatField(max_length=20)
    inv_disc = models.FloatField(max_length=20)
    inv_fees = models.IntegerField()
    inv_misc_fees = models.IntegerField()

    # timestemps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)