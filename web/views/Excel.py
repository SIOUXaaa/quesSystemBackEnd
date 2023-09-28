import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from web.models import SurveyResponses
from web.serializers.SurveyResponses import SurveyResponsesSerializer


class ExcelView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request):
        project = request.GET.get('project')
        survey_responses = SurveyResponses.objects.filter(project=project)

        serializer = SurveyResponsesSerializer(survey_responses, many=True)

        data = list(survey_responses.values())
        converted_data = []

        print(data)
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

        excel_file = '/home/sercoi/FintechRa/backEnd/quesSystemBackEnd/web/excel/'+project+'.xlsx'
        df.to_excel(excel_file, index=False)

        response = Response(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = f"attachment;filename={project}.xlsx"

        with open(excel_file, "rb") as f:
            response.write(f.read())

        return response
