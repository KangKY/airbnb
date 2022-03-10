from rest_framework.permissions import BasePermission

class IsHost(BasePermission):
  def has_object_permission(self, request, view, reservation):
    return reservation.room.host == request.user

class IsGuest(BasePermission):
  def has_object_permission(self, request, view, reservation):
    print(view)
    return reservation.guest == request.user