import datetime
from rest_framework import serializers
from web.models import Question


class QuestionSerializer(serializers.Serializer):
    question_id = serializers.CharField(max_length=255)
    user_id = serializers.CharField(max_length=255)
    answer = serializers.JSONField()
    ip = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        question = Question(**validated_data)
        question.time = datetime.datetime.now()
        question.save()
        return question
    
    class Meta:
        model = Question
        fields = ['question_id', 'user_id', 'answer', 'ip']