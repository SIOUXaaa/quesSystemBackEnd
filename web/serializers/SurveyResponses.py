import datetime
from django.utils import timezone
from rest_framework import serializers
from web.models import SurveyResponses, Project
from django.conf import settings


class SurveyResponsesSerializer(serializers.Serializer):
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all())
    user_id = serializers.CharField(max_length=255)
    answer = serializers.JSONField()
    ip = serializers.CharField(max_length=255, required=False)
    time = serializers.CharField(required=False)

    def create(self, validated_data):
        survey_responses = SurveyResponses(**validated_data)
        survey_responses.save()
        return survey_responses

    class Meta:
        model = SurveyResponses
        fields = ['project', 'user_id', 'answer', 'ip', 'time']
