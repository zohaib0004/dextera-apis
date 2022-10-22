from rest_framework import serializers
from ..models.firm import BillingAddress, Firm, PaymentInfo
from django.contrib.auth import get_user_model
 
User = get_user_model()

class UploadFirmLogo(serializers.ModelSerializer):
    class Meta:
        model= Firm
        fields = (
            'id',
            'logo',
        )

class GetFirmAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields =  ('id',
                    'owner',
                    'logo',
                    'c_name',
                    'website',
                    'office',
                    'c_street',
                    'c_suite',
                    'c_city',
                    'c_state',
                    'c_zip',
                    'c_ext')

# create new firm on registerations 
class CreateFirmAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields =  ('id',
                    'owner',
                    'c_name',
                    'dba_name',
                    'tax_id',
                    'tax_id_ext',
                    'website',
                    'office',
                    'c_street',
                    'c_suite',
                    'c_city',
                    'c_state',
                    'c_zip',
                    'c_ext'
                    )

class GetBillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = (
            'id',
            'user')

class GetPaymentInfoSerializer(serializers.ModelSerializer):   
    class Meta:
        model = PaymentInfo
        fields = (
            'id',
            'user',
            
            )
class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = (
            "id",
            "user",
            "account_name",
            "account_no",
            "bank_name",
            "rounting",
            "credit_card",
            "card_no",
            "security_id",
            "expire_date",
        )

class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = (
            'id',
            'is_monthly',
            'plan',
            'street',
            'suite',
            'city',
            'state',
            'zip',
            'ext')
    

