from io import BytesIO
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_simplejwt.authentication import JWTAuthentication
from web.Authentication import MyJWTAuthentication

from web.models import SurveyResponses
from django.http import StreamingHttpResponse


class ExcelView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    authentication_classes = [MyJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        project = request.GET.get('project')
        survey_responses = SurveyResponses.objects.filter(project=project)

        # 数据解析
        data = list(survey_responses.values())
        converted_data = []
        for item in data:
            converted_item = {
                "project":  item['project_id'],
                "user_id": item['user_id'],
                "ip": item['ip'],
                "time": item['time'],
            }
            converted_item['time'] = converted_item['time'].strftime(
                "%Y-%m-%d %H:%M:%S")
            converted_item.update(item['answer'])
            converted_data.append(converted_item)

        df = pd.DataFrame(converted_data)

        excel_file = BytesIO()
        df.to_excel(excel_file, index=False)

        # 重置文件指针
        excel_file.seek(0)

        # 设置下载xlsx相关的response属性
        response = StreamingHttpResponse(excel_file,
                                         content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f"attachment;filename={project}.xlsx"
        response['Access-Control-Expose-Headers'] = 'Content-Disposition'

        return response
