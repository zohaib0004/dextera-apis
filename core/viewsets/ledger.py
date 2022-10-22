from ..models.ledger import LedgerTime
from rest_framework import viewsets, permissions

from ..serializers.ledger import NewLedgerTimeSerializer

class NewLedgerTimeViewset(viewsets.ModelViewSet):
    queryset = LedgerTime.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewLedgerTimeSerializer