from django.views.generic import base
from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
  path("", views.RoomsView.as_view()),
  path("<int:pk>/", views.RoomView.as_view())
]
