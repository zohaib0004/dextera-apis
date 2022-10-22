from rest_framework import serializers
from ..models.ledger import LedgerTime


class NewLedgerTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerTime
        fields =  (
            "contact",
            "matter_name",
            "category",
            "sub_category",
            "hard",
            "soft",
            "unit",
            "qty",
            "rate",
            "time",
            "date",
            "detail",
            "bill_by",
            "billable",
            "note",
        )