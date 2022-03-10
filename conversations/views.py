from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConversationSerializer, MessagesSerializer
from .models import Conversation, Message
from .permissions import IsParticipants

# Create your views here.


class ConversationViewSet(ModelViewSet):
  queryset = Conversation.objects.all()
  serializer_class = ConversationSerializer

  def get_permissions(self):
    if self.action =="create" and self.action == 'list':
      permission_classes = [IsAuthenticated]
    else:
      permission_classes = [IsAuthenticated, IsParticipants]
    
    return [permission() for permission in permission_classes]

  @action(detail=True)
  def messages(self, request, pk):
    conversation = self.get_object()
    serializer = MessagesSerializer(conversation.messages.all(), many=True, context={"request": request}).data
    return Response(serializer)

  @messages.mapping.post
  def send_message(self, request, pk):
    if pk is not None:
      try:
        message_text = request.data.get("message", None)
        conversation = Conversation.objects.get(pk=pk)
        if message_text is not None:
          message = Message.objects.create(conversation=conversation, message=message_text, user=request.user)
          serializer = MessagesSerializer(message).data
          return Response(serializer)
        else:
          return Response(status=status.HTTP_402_PAYMENT_REQUIRED)
      except conversation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)



# class MessagesViewSet(ModelViewSet):
#   queryset = Message.objects.all()
#   serializer_class = MessagesSerializer
  
#   # def get_permissions(self):
#   #   if self.action =="create" and self.action == 'list':
#   #     permission_classes = [IsParticipants]
#   #   else:
#   #     permission_classes = [IsParticipants]
    
#   #   return [permission() for permission in permission_classes]
    