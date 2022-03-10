from rest_framework.permissions import BasePermission

class IsParticipants(BasePermission):
  def has_object_permission(self, request, view, conversation):
    return request.user in conversation.participants.all()