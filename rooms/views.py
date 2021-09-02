from functools import partial
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer

# django에서 처리하는 것보다 rest_framework을 통해 처리하면
# POST데이터를 자동으로 dictionary로 바꾸는 등 여러 기능을 수행해줌.
# @api_view(["GET","POST"])
# def rooms_view(request):
#   if request.method == "GET":
#     rooms = Room.objects.all()[:3]
#     serializer = ReadRoomSerializer(rooms, many=True).data
#     return Response(serializer)
#   elif request.method == "POST":
#     if not request.user.is_authenticated:
#       return Response(status=status.HTTP_401_UNAUTHORIZED)
#     serializer = WriteRoomSerializer(data=request.data)
#     if serializer.is_valid():
#       room = serializer.save(user=request.user)
#       room_serializer = ReadRoomSerializer(room).data
#       return Response(data=room_serializer, status=status.HTTP_201_CREATED)
#     else:
#       return Response(status=status.HTTP_400_BAD_REQUEST)

# Remove GenericView
# class ListRoomsView(ListAPIView):
#   queryset = Room.objects.all()
#   serializer_class = RoomSerializer
# class SeeRoomView(RetrieveAPIView):
#   queryset = Room.objects.all()
#   serializer_class = ReadRoomSerializer

class RoomsView(APIView):
  def get(self, request):
    rooms = Room.objects.all()[:3]
    serializer = RoomSerializer(rooms, many=True).data
    return Response(serializer)
  def post(self, request):
    if not request.user.is_authenticated:
      return Response(status=status.HTTP_401_UNAUTHORIZED)
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
      room = serializer.save(user=request.user)
      room_serializer = RoomSerializer(room).data
      return Response(data=room_serializer, status=status.HTTP_201_CREATED)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)

class RoomView(APIView):
  def get_room(self, pk):
    try:
      room = Room.objects.get(pk=pk)
      return room
    except Room.DoesNotExist:
      return None

  def get(self, request, pk):
    room = self.get_room(pk)
    if room is not None:
      serializer = RoomSerializer(room).data
      return Response(serializer)
    else:
      return Response(status=status.HTTP_404_NOT_FOUND)
      
  def put(self, request, pk):
    room = self.get_room(pk)
    if room is not None:
      if room.user != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
      serializer = RoomSerializer(room, data=request.data, partial=True)
      if serializer.is_valid():
        room = serializer.save()
        return Response(data=RoomSerializer(room).data, status=status.HTTP_200_OK)
      else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response(status=status.HTTP_404_NOT_FOUND)

  def delete(self, request, pk):
    room = self.get_room(pk)
    if room is not None:
      if room.user != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
      room.delete()
      return Response(status=status.HTTP_200_OK)
    else:
      return Response(status=status.HTTP_404_NOT_FOUND)


