from django.views.generic import base
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from .viewsets import RoomViewSet
app_name = 'rooms'

router = DefaultRouter()
router.register("", RoomViewSet, basename='room')


# urlpatterns = [
#   path("list/", views.ListRoomsView.as_view()),
#   path("<int:pk>/", views.SeeRoomView.as_view())
# ]

urlpatterns = router.urls