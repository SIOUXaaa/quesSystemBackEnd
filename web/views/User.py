from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from web.models import User
from web.serializers.User import UserSerializer
from rest_framework.decorators import api_view

from web.utils.jwt import generate_token


class LoginView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            # user = authenticate(username=username, password=password)
            user = User.objects.get(username=username)
            if user.password == password:
            # if user is not None:
                token = generate_token(user)
                return Response({'msg': 'success', 'token': token.get("access")}, status=status.HTTP_200_OK)
            else:
                return Response({"msg": 'password error'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"msg": 'user not exist'}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.validated_data['password'] = make_password(request.data['password'])
            serializer.save()
            return Response({'msg': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
