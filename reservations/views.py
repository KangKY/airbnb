from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ReservationSerializer
from .models import Reservation
from .permissions import IsHost, IsGuest

# Create your views here.


class ReservationViewSet(ModelViewSet):
  queryset = Reservation.objects.all()
  serializer_class = ReservationSerializer

  def get_permissions(self):
    if self.action == 'list' and self.action =="create":
      permission_classes = [IsAuthenticated]
    else:
      permission_classes = [IsHost | IsGuest]
    
    return [permission() for permission in permission_classes]
  

    