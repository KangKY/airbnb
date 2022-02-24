import jwt
from users.models import User
from django.conf import settings
from jwt.exceptions import DecodeError
from rest_framework import authentication, exceptions

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
      try:
        token = request.META.get('HTTP_AUTHORIZATION')
        if token is None:
            return None
        _, jwt_token = token.split(" ")
        decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
        pk = decoded.get('pk')
        user = User.objects.get(pk=pk)
        return (user, None)
      
      except (ValueError, jwt.exceptions.DecodeError, User.DoesNotExist):
        return None
      # except jwt.exceptions.DecodeError:
      #   raise exceptions.AuthenticationFailed(detail="JWT Format Decode Error")
      # except jwt.exceptions.InvalidTokenError:
      #   raise exceptions.AuthenticationFailed(detail="JWT Format Invalid")
      # except jwt.exceptions.ExpiredSignatureError:
      #   raise exceptions.AuthenticationFailed(detail="JWT Expired")
      # except User.DoesNotExist:
      #   raise exceptions.AuthenticationFailed('No such user')
