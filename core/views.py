# from django.core import serializers
# from django.http import HttpResponse
# from rooms.models import Room
# # Create your views here.

# def list_rooms(request):
#   rooms = serializers.serialize("json", Room.objects.all())
#   res = HttpResponse(content=rooms)
#   return res