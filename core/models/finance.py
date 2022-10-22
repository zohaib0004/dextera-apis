from django.db import models

from accounts.models import UserAccount


class FinanceAccount(models.Model):
    owner = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name="finance_account", blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Subscription(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="subcription", blank=True, null=True)
    plan = models.CharField(max_length=255)
    cycle = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    validate_in_days = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_renewal = models.BooleanField(default=False)
    is_upgrade = models.BooleanField(default=False)
    is_downgrade = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# it keeps the record of transactions of each user and return revenue in and revenue out 
class TransactionHistory(models.Model):
    to = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING, related_name="transaction_to", blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    by = models.ForeignKey(UserAccount,  on_delete=models.DO_NOTHING, related_name="transaction_by", blank=True, null=True)

    is_credit = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


