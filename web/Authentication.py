from typing import Any, Dict
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _

from web.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        authenticate_kwargs = {self.username_field: attrs[self.username_field], 'password': attrs['password']}
        # print("==========", authenticate_kwargs)
        try:
            user = User.objects.get(**authenticate_kwargs)
        except Exception as e:
            raise exceptions.NotFound(e.args[0])
        
        
        refresh = self.get_token(user)
        
        data = {"username":user.username, "token":str(refresh.access_token)}
        return data
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class MyJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token['user_id']
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise AuthenticationFailed(_('User not found'), 401)     
