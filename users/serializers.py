from django.db.models import fields
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ('password', 'user_permissions', 'groups', 'is_active', "favs",
               "is_staff", "is_superuser", "last_login", "date_joined")

class TinyUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username','avatar','superhost')
