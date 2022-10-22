
from django.core.management import BaseCommand
from core.models.finance import Subscription
from core.models.profile import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    # Show this when the user types help
    help = "Create Role and its permissions"

    # A command must define handle()
    def handle(self, *args, **options):
   
        u1 = User.objects.create_client(username="firm1", first_name="Sherlock", last_name="Holmes", email="firm1@firm1.com", password="firm11234")
        print("Creating {}".format(u1))
        u1.save

        u2 = User.objects.create_client(username="firm2", first_name="Mycroft", last_name="Holmes", email="firm2@firm2.com", password="firm21234" )
        print("Creating {}".format(u2))
        u2.save
       
        u3 = User.objects.create_firm_employee(username="lawyer1", first_name="John", last_name="Watson", email="lawyer1@firm1.com", password="lawyer11234")
        print("Creating {}".format(u3))
        u3.save

        u4 = User.objects.create_firm_employee(username="lawyer2", first_name="Greg", last_name="Lestrade", email="lawyer2@firm2.com", password="lawyer21234")
        print("Creating {}".format(u4))
        u4.save
       
        u5 = User.objects.create(username="user", first_name="James", last_name="Moriarty", email="user@firm2.com", password="user1234" )
        print("Creating {}".format(u5))
        u5.save

        m1 = Profile.objects.create(user=u1, first_name="Sherlock", last_name="Holmes", c_email="firm1@firm1.com", group="firm", role="Director")
        print("Creating {}".format(u1))
        m1.save

        sub1 = Subscription.objects.create(user = u1)
        print("Creating Subscription {}".format(sub1))
        sub1.save

        m2 = Profile.objects.create(user=u2, first_name="Mycroft", last_name="Holmes", c_email="firm2@firm2.com",  group="firm", role="Director")
        print("Creating {}".format(u2))
        m2.save

        sub2 = Subscription.objects.create(user = u2)
        print("Creating Subscription {}".format(sub2))
        sub2.save       

        m3 = Profile.objects.create(user=u3, first_name="John", last_name="Watson", c_email="lawyer1@firm1.com", group="lawyer", role="Sr. Atterney")
        print("Creating {}".format(u3))
        m3.save
        
        sub3 = Subscription.objects.create(user = u3)
        print("Creating Subscription {}".format(sub3))
        sub3.save

        m4 = Profile.objects.create(user=u4, first_name="Greg", last_name="Lestrade", c_email="lawyer2@firm2.com", group="lawyer", role="Sr. Atterney")
        print("Creating {}".format(u4))
        m4.save
        sub4 = Subscription.objects.create(user = u4)
        print("Creating Subscription {}".format(sub4))
        sub4.save

        m5 = Profile.objects.create(user=u5, first_name="James", last_name="Moriarty", c_email="user@firm2.com", group="client", role="")
        print("Creating {}".format(u5))
        m5.save

        sub5 = Subscription.objects.create(user = u5)
        print("Creating Subscription {}".format(sub5))
        sub5.save