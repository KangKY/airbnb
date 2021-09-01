from rest_framework import serializers
from users.serializers import TinyUserSerializer, UserSerializer
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  class Meta:
    model = Room
    exclude = ("modified",)
