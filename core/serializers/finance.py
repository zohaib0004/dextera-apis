from  core.models.finance  import FinanceAccount, Subscription, TransactionHistory
from accounts.models import UserAccount

from rest_framework import serializers

class FinanceAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= FinanceAccount
        fields= ("id", "owner", "balance")

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields =("__all__")

class IsSubscriptionActiveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscription
        fields =("user", "is_active")

class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model= TransactionHistory
        fields= ("id", # need to do a better job in transaction and bankaccount 
                "to",
                "amount",
                "by",
                "is_credit",
                "created_at")
        def create(self, validated_data):
            amount = validated_data['amount']
            trans_by = UserAccount.objects.get(id = validated_data["by"])
            trans_to = UserAccount.objects.get(id = validated_data["to"])
            
            account_by, create = FinanceAccount.objects.get_or_create(owner = validated_data["by"])
            account_to, create = FinanceAccount.objects.get_or_create(owner = validated_data["to"])

            account_to.balance += amount
            account_to.save()
            account_by.balance -= amount
            account_by.save()
            transHistory = TransactionHistory.objects.create(
                to = trans_to,
                amount = amount ,
                by = trans_by,
                is_credit = True
                )
            transHistory.save()

        