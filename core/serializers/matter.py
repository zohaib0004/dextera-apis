from rest_framework import serializers
from ..models.matter import Matter, Task


class NewMatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matter
        fields = (
            "contact",
            "matter_name",
            "matter_type",
            "matter_source",
            "matter_status",
            "assign_to",
            "assign_by",
            "billing_rate",
            "alerts",
            "open_date",
            "close_date",
            "total_days",
            "jurisdiction",
            "status_limitaion",
            "opposing_counsel",
            "where",
            "when",
            "involved",
            "witnesses",
            "narrative",
        )
class MatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matter
        fields =  (
            "id",
            "contact",
            "matter_name",
            "matter_type",
            "matter_source",
            "matter_status", # open close 
            "assign_to",
            "assign_by", # by firm 
        )

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model: Task
        fields = (
            "matter_id",
            "matter_contact",
            "matter",
            "is_billable",
            "is_private",
            "task",
            "detail",
            "file",
            "assign_to",
            "status",
            "task_nature",
            "due_at",
        )
class TasksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields= (
            "id", 
            "task_nature",
            
            "matter", 
            "last_action", 
            "next_action", 
            "assign_to", 
            "due_at"
        )
class NewTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields= (
            "matter_id",
            "matter_contact", 
            "matter",
            "task", 
            "file", 
            "is_billable", 
            "is_private", 
            "due_at", 
            "assign_to", 
            "detail",
        )
