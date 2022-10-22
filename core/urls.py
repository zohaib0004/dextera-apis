
from  django.urls import path

from core.viewsets.finance import FinanceAccountViewsets, IsSubscriptionViewset, RevenueInViewsets, RevenueOutViewsets, SubscriptionViewset, TransactionHistoryViewsets

from .viewsets.contact import ContactViewset
from .viewsets.ledger import NewLedgerTimeViewset
from .viewsets.profile import ProfileList, CreateMemberViewset,  ProfileRegViewSet, MembersViewset, GetProfileViewSet, UpdateProfileViewSet
from .viewsets.firm import GetFirmAccountViewset, GetPaymentInfoViewset,GetBillingAddressViewset,PaymentInfoViewset,BillingAddressViewset, UploadFirmLogoViewset
from .viewsets.matter import MatterList, TaskViewset, TasksViewset, NewMatterViewset, NewTaskViewset
from .viewsets.category import CategoryViewset, SubCategoryViewset, ClassificationViewset
from .viewsets.member import ListMembersView, UpdateMemberView
from .viewsets.firm import FirmAccountViewset, GetFirmDetailViewSet, GetFirmSummaryViewSet

from rest_framework import routers

router = routers.DefaultRouter()

# register user 
router.register('profile', ProfileList, 'profile')
router.register('update-profile', UpdateProfileViewSet, 'update-profile')
router.register('get-profile', GetProfileViewSet, 'get-profile')
router.register('get-subscription', SubscriptionViewset, 'get-subscription')
router.register('is-subscription', IsSubscriptionViewset, 'is-subscription')

# register firm 
router.register('get-firm', GetFirmAccountViewset, 'get-profile')
router.register('create-firm', FirmAccountViewset, 'create-firm')
router.register('get-payment-info-reg', GetPaymentInfoViewset, 'get-payment-info')
router.register('get-bill-add-reg', GetBillingAddressViewset, 'get-bill-add')
router.register('payment-info-reg', PaymentInfoViewset, 'payment-info-reg')
router.register('bill-add-reg', BillingAddressViewset, 'bill-add-reg')
router.register('upload-logo', UploadFirmLogoViewset, 'upload-logo')

# finance Urls 
router.register('finance-account', FinanceAccountViewsets, "finance_accout") 
# router.register('finance-summary', GetRevenueViewset, "finance_summary") 
router.register('revenue-in', RevenueInViewsets, "revenue_in")
router.register('revenue-out', RevenueOutViewsets, "revenue_out")
router.register('transaction-history', TransactionHistoryViewsets, "transaction-history")


router.register('profile-reg', ProfileRegViewSet, 'profile-reg')
router.register('firm-detail', GetFirmDetailViewSet, 'firm-detail')
router.register('firm-summary', GetFirmSummaryViewSet, 'firm-summary')
router.register('matter', MatterList, "matter")

router.register('new-matter', NewMatterViewset, "new-matter")

router.register('category', CategoryViewset, "category")
router.register('sub-category', SubCategoryViewset, "sub-category")
router.register('classification', ClassificationViewset, "classification")

router.register('tasks', TasksViewset, "tasks" )
router.register('task', TaskViewset, "task")
router.register('new-task', NewTaskViewset, "task")

router.register('add-time',NewLedgerTimeViewset, 'add-time')
router.register('members', MembersViewset, "members")
router.register('create-member', CreateMemberViewset, "create-member")

router.register('contact', ContactViewset, "contact")
# router.register('members-lists', ListMembersView.as_view(), "member-list")

urlpatterns = router.urls + [
    path('members-list/', ListMembersView.as_view()),
    path('member-update/<int:pk>/', UpdateMemberView.as_view()),
    # path('upload-logo/', UploadFirmLogoViewset.as_view()),
    # path('create-firm/', CreateFirmAccountViewSet.as_view())
]