# Create your views here.
from ..models.matter import Matter, Task
from rest_framework import  viewsets, permissions
from ..serializers.matter import MatterSerializer,NewMatterSerializer, TaskCreateSerializer, TasksListSerializer, NewTaskSerializer
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404



#  for creating and viewing single item 
class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TaskCreateSerializer


# for general view or list 
class TasksViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TasksListSerializer

# for creating new matter and store it into database 
class NewMatterViewset(viewsets.ModelViewSet):
    queryset = Matter.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewMatterSerializer


class NewTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewTaskSerializer

# for retriving data a limited information about matter to list it out 
class MatterList(viewsets.ModelViewSet):
    queryset = Matter.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MatterSerializer
    # def retrieve(self, request, pk=None):
    #     queryset = Matter.objects.get(pk=pk)
    #     profile = get_object_or_404(queryset, pk=1)
    #     serializer = MatterSerializer(profile)
    #     return Response(serializer.data)
    

# # access detailed view 
# class MatterDetailViewset(viewsets.ModelViewSet):
#         serializer_class = MatterSerializer

#         def get_queryset(self):
#             username = self.kwargs['username']
#             return Matter.objects.get(profile__username=username)
        
        