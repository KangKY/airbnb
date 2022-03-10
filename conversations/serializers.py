from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Conversation, Message

class MessagesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ("message","user","created")


  # def create(self, validated_data):
  #   request =  self.context.get("request")
  #   message = Message.objects.create(**validated_data, user=request.user)
  #   return message

class ConversationSerializer(serializers.ModelSerializer):
  messages = MessagesSerializer(read_only=True, many=True)
  participants = UserSerializer(read_only=True, many=True)
  class Meta:
    model = Conversation
    fields = (
      "id",
      "participants",
      "messages"
    )

