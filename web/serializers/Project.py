import datetime
from django.utils import timezone
from rest_framework import serializers
from web.models import Project
from django.conf import settings

#Project model对应的serializers
class ProjectSerializer(serializers.Serializer):
    project_id = serializers.CharField(max_length=255)
    project_name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)

    def create(self, validated_data):
        project = Project(**validated_data)
        project.save()
        return project
    
    def update(self, instance, validated_data):
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.project_name = validated_data.get('project_name', instance.project_name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    
    class Meta:
        model = Project
        fields = ['project_id', 'project_name', 'description']