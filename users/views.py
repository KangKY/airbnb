import jwt
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rooms.models import Room
from rooms.serializers import RoomSerializer
from .serializers import UserSerializer, PasswordSerializer
from .models import User
from .permissions import IsSelf


class UsersViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_permissions(self):
    if self.action == 'list':
      permission_classes = [IsAdminUser]
    elif self.action == 'create' or self.action == 'retrieve' or self.action == 'favs' or self.action == 'login':
      permission_classes = [AllowAny]
    else:
      permission_classes = [IsSelf]
    return [permission() for permission in permission_classes]

  @csrf_exempt
  @action(methods=["POST"], detail=False)
  def login(self, request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
      return Response(status=status.HTTP_400_BAD_REQUEST)
    #user = authenticate(email=email, password=password)
    user = authenticate(email=email, password=password)
    if user is not None:
      encoded_jwt = jwt.encode(
          {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256")
      return Response(data={'token': encoded_jwt, 'id': user.pk})
    else:
      return Response(status=status.HTTP_401_UNAUTHORIZED)

  @action(detail=True)
  def favs(self, request, pk):
    user = self.get_object()
    serializer = RoomSerializer(user.favs.all(), many=True, context={
                                "request": request}).data
    return Response(serializer)

  @favs.mapping.put
  def toggle_favs(self, request, pk):
    pk = request.data.get("pk", None)
    user = request.user
    if pk is not None:
      try:
        room = Room.objects.get(pk=pk)
        if room in user.favs.all():
          user.favs.remove(room)
        else:
          user.favs.add(room)
        return Response()
      except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)


  @action(detail=True, methods=['post'])
  def set_password(self, request, pk=None):
      user = self.get_object()
      serializer = PasswordSerializer(data=request.data)
      if serializer.is_valid():
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response({'status': 'password set'})
      else:
          return Response(serializer.errors,
                          status=status.HTTP_400_BAD_REQUEST)

  @action(detail=False)
  def recent_users(self, request):
    recent_users = User.objects.all().order_by('-last_login')

    page = self.paginate_queryset(recent_users)
    if page is not None:
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(recent_users, many=True)
    return Response(serializer.data)
