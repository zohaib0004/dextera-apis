from ..models.profile import Profile

from rest_framework import generics, permissions 
from rest_framework.views import APIView
from ..serializers.profile import MembersSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ListMembersView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = MembersSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UpdateMemberView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = MembersSerializer

@method_decorator(csrf_exempt, name='dispatch')
class DeleteMemberView(generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = MembersSerializer
