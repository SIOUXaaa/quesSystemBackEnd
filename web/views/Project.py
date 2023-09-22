from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from web.models import Project
from web.serializers.Project import ProjectSerializer


class ProjectView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request):
        project_id = request.GET.get('project_id')
        project = Project.objects.get(pk=project_id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 修改project信息，包括project_name, description
    def put(self, request):
        project_id = request.POST.get('project_id')
        project = Project.objects.get(pk=project_id)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        project_id = request.GET.get('project_id')
        project = Project.objects.get(pk=project_id)
        project.delete()
        return Response({'msg': 'success'}, status=status.HTTP_200_OK)
