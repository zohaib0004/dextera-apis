from rest_framework import serializers
from ..models.contact import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields =  (
            "company_name",
            "webiste",
            "ger_email",
            "billing_email",
            "street",
            "suite",
            "city",
            "state",
            "zip",
            "plus_4",
            "client_no",
            "f_name",
            "l_name",
            "dob",
            "ssn",
            "mobile_no",
            "home_no",
            "office_no",
            "fax_no",
            "other_no",
            "email_1",
            "email_2",
            "email_3",
            "street2",
            "suite2",
            "city2",
            "state2",
            "zip2",
            "plus_42",
            "office",
            "team",
            "member",
            "assign_to",
            "contact",
            "relation",
        )
