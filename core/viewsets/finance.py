from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.response import Response
from ..models.firm import Firm
from core.models.finance import FinanceAccount, Subscription, TransactionHistory
from core.serializers.finance import FinanceAccountSerializer, IsSubscriptionActiveSerializer, SubscriptionSerializer, TransactionHistorySerializer
from accounts.models import UserAccount
from django.db.models import Sum


class FinanceAccountViewsets(viewsets.ModelViewSet):
    queryset = FinanceAccount.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FinanceAccountSerializer

    def get_queryset(self):
    
        queryset = FinanceAccount.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = FinanceAccount.objects.filter(owner=user)
        return queryset

    


class IsSubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IsSubscriptionActiveSerializer

    def get_queryset(self):
        queryset = Subscription.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = Subscription.objects.filter(user=user)
        return queryset

class SubscriptionViewset(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = SubscriptionSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # accessing current user finance account 
        user_finance = FinanceAccount.objects.get(owner = self.request.user.id)
        
        # accessing admin account and its finace account 
        admin = UserAccount.objects.get(is_superuser = True)
        admin_finacne = FinanceAccount.objects.get(owner = admin)

        if serializer.is_valid():
            current_user = self.request.user.id
            plan = serializer.validated_data['plan']
            cycle = serializer.validated_data['cycle']
            amount = serializer.validated_data['amount']
            is_active =True
            sub = Subscription.objects.create(user=current_user, plan= plan, cycle=cycle, amount = amount, is_active= is_active)
            sub.save()
         
            # it will change the 
            user_finance.balance -= amount
            admin_finacne.balance += amount
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        queryset = Subscription.objects.all()
        user = self.request.query_params.get('user')
        
        if user is not None:
            queryset = Subscription.objects.filter(user=user)
        return queryset

class TransactionHistoryViewsets(viewsets.ModelViewSet):
    queryset = TransactionHistory.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionHistorySerializer
    def get_queryset(self):
        queryset = TransactionHistory.objects.all()
        user = self.request.query_params.get('user')
        
        if user is not None:
            queryset = TransactionHistory.objects.filter(to=user)
        return queryset
    

class RevenueInViewsets(viewsets.ModelViewSet):
    queryset = TransactionHistory.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionHistorySerializer
    def get_queryset(self):
        queryset = TransactionHistory.objects.all()
        user = self.request.query_params.get('user')
        
        if user is not None:
            queryset = TransactionHistory.objects.filter(to=user)
        return queryset

class RevenueOutViewsets(viewsets.ModelViewSet):
    queryset = TransactionHistory.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionHistorySerializer
    def get_queryset(self):
        queryset = TransactionHistory.objects.all()
        user = self.request.query_params.get('user')
        
        if user is not None:
            queryset = TransactionHistory.objects.filter(by=user)
        return queryset



# class GetRevenueViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = TransactionHistory.objects.all()
#     permission_classes = [permissions.AllowAny] # change persmissions
#     serializer_class = TransactionHistorySerializer

#     def get_queryset(self):
#         queryset = TransactionHistory.objects.all()
#         user = self.request.query_params.get('user')
        
#         if user is not None:
#             queryset = TransactionHistory.objects.filter(to=user)
#         return queryset

#     def retrieve(self, request, *args, **kwargs):
#         current_user = self.request.user.id
#         if current_user is not None:
#             current_balance = FinanceAccount.objects.get(owner = current_user)
#             revenueIn = TransactionHistory.objects.filter(to = current_user, is_credit = True).aggregate(Sum('amount'))
#             revenueOut = TransactionHistory.objects.filter(by = current_user, is_credit = True).aggregate(Sum('amount'))
#             expectedBalnace = TransactionHistory.objects.filter(by = current_user, is_credit = False).aggregate(Sum('amount'))

#             return Response({
#                 "current_balance" : current_balance,
#                 "revenueIn": revenueIn,
#                 "revenueOut": revenueOut,
#                 "expectedBalnace" : expectedBalnace,
#                 "status": status.HTTP_200_OK
#                 }) 
#         return Response(status=status.HTTP_400_BAD_REQUEST)
