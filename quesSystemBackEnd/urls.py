"""quesSystemBackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from web.views.SurveyResponses import SurveyResponsesView
from web.views.Project import ProjectView
from web.views.Excel import ExcelView
from web.views.User import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surveyResponses/get/', SurveyResponsesView.as_view()),
    path('surveyResponses/post/', SurveyResponsesView.as_view()),
    path('project/get_all/', ProjectView.as_view()),
    path('project/get/', ProjectView.as_view()),
    path('project/post/', ProjectView.as_view()),
    path('project/put/', ProjectView.as_view()),
    path('project/delete/', ProjectView.as_view()),
    path('excel/get/', ExcelView.as_view()),
    path('user/login/', LoginView.as_view()),
    path('user/register/', RegisterView.as_view())
]
