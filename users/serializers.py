from django.db.models import fields
from rest_framework import serializers
from .models import User


class RelatedUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      "username",
      "first_name",
      "last_name",
      "email",
      "avatar",
      "superhost"
    )

class ReadUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    exclude = ('password', 'user_permissions', 'groups', 'is_active',
               "is_staff", "is_superuser", "last_login", "date_joined", "favs")

class WriterUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = (
      "username",
      "first_name",
      "last_name",
      "email"
    )

  def validate_first_name(self, value):
      print(value)
      return value.upper()