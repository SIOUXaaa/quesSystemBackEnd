from django.http import QueryDict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from web.models import Project, SurveyResponses
from web.serializers.SurveyResponses import SurveyResponsesSerializer
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'current_page'
    max_page_size = 100


# Create your views here.
class SurveyResponsesView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request):
        project = request.GET.get('project')
        survey_responses = SurveyResponses.objects.all()

        if project:
            survey_responses = survey_responses.filter(project=project)

        for s in survey_responses:
            s.time = timezone.localtime(s.time)

        paginator = Pagination()
        paginated_SurveyResponses = paginator.paginate_queryset(
            survey_responses, request)
        serializer = SurveyResponsesSerializer(
            paginated_SurveyResponses, many=True)

        response = paginator.get_paginated_response(serializer.data)
        response.data['total'] = paginator.page.paginator.count  # 添加当前查询的数据条数

        return Response(response.data, status=status.HTTP_200_OK)

    def post(self, request):
        project = request.data.get('project')
        print(request.data)
        print(project)
        # 查询 project表是否存在project_id
        project = Project.objects.filter(pk=project)
        if not project:
            return Response({'msg:': 'project not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SurveyResponsesSerializer(data=request.data)
        serializer.project = project
        if serializer.is_valid():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            serializer.validated_data['ip'] = ip
            serializer.save()
            return Response({'msg:': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
