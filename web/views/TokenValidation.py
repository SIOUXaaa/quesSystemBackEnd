from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import IsAuthenticated
from web.Authentication import MyJWTAuthentication
from rest_framework import status



class TokenValidationView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    authentication_classes = [MyJWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        # 令牌验证
        return Response({'detail': 'Authenticated user'}, status=status.HTTP_200_OK)
