from rest_framework_simplejwt.tokens import RefreshToken

def generate_token(user):
    print(user)
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }