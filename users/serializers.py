from django.db.models import fields
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = (
      "id",
      "username",
      "first_name",
      "last_name",
      "email",
      "avatar",
      "superhost",
      "password"
    )
    #extra_kwargs = {'password': {'write_only': True}}
    read_only_fields = ("id", "superhost", "avatar")

  def validate_first_name(self, value):
      print(value)
      return value.upper()

  def create(self, validated_data):
      user = super().create(validated_data)
      user.set_password(validated_data['password'])
      user.save()
      return user
      