from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from web.Authentication import MyJWTAuthentication

from web.models import Project
from web.serializers.Project import ProjectSerializer


class ProjectView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    authentication_classes = [MyJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        project_id = request.GET.get('project_id')

        if project_id:
            try:
                project = Project.objects.get(pk=project_id)
            except:
                return Response({'msg': 'project not exist'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 修改project信息，包括project_name, description
    def put(self, request):
        project_id = request.data.get('project_id')
        try:
            project = Project.objects.get(pk=project_id)
        except:
            return Response({'msg': 'project not exist'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectSerializer(project, data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        project_id = request.GET.get('project_id')
        try:
            project = Project.objects.get(pk=project_id)
        except:
            return Response({'msg': 'project not exist'}, status=status.HTTP_400_BAD_REQUEST)

        if project:
            project.delete()
            return Response({'msg': 'success'}, status=status.HTTP_200_OK)

        return Response({'msg': 'project not exist'}, status=status.HTTP_400_BAD_REQUEST)
