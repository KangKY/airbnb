from django.db.models import fields
from rest_framework import serializers
from rooms.models import Room, Photo


#from rooms.serializers import RoomSerializer
from .models import User

class PhotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Photo
    fields = ('file', 'caption')

class UserRoomSerializer(serializers.ModelSerializer):

  photos = PhotoSerializer(read_only=True, many=True)
  class Meta:
    model = Room
    fields = (
      "id",
      "name",
      "address",
      "price",
      "beds",
      "lat",
      "lng",
      "bedrooms",
      "bathrooms",
      "check_in",
      "check_out",
      "instant_book",
      "photos",
    )

class UserSerializer(serializers.ModelSerializer):
  
  password = serializers.CharField(write_only=True)
  rooms = UserRoomSerializer(read_only=True, many=True)

  class Meta:
    model = User

    fields = (
      "id",
      "username",
      # "first_name",
      # "last_name",
      "email",
      "avatar",
      "superhost",
      "password",
      "room_count",
      "rooms"
    )
    #extra_kwargs = {'password': {'write_only': True}}
    read_only_fields = ("id", "superhost", "avatar")

  def validate_first_name(self, value):
      return value.upper()

  def create(self, validated_data):
    print(validated_data)
    user = super().create(validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user
    