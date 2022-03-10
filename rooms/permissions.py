from rest_framework.permissions import BasePermission
'''
.has_permission(self, request, view) : 리스트나 개별 object에 적용 
.has_object_permission(self, request, view, obj) : 개별 object에만 적용 (rooms/1)
'''
class IsOwner(BasePermission):
  def has_object_permission(self, request, view, room):
    return room.host == request.user