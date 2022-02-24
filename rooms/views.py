from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Room
from .permissions import IsOwner
from .serializers import RoomSerializer

# django에서 처리하는 것보다 rest_framework을 통해 처리하면
# POST데이터를 자동으로 dictionary로 바꾸는 등 여러 기능을 수행해줌.

class RoomViewSet(ModelViewSet):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer
  
  def get_permissions(self):
    if self.action == 'list' or self.action == "retrieve":
      permission_classes = [AllowAny]
    elif self.action == 'create':
      permission_classes = [IsAuthenticated]
    else:
      permission_classes = [IsOwner]
    return [permission() for permission in permission_classes]

  @action(detail=False)
  def search(self, request):
    keyword = request.GET.get('keyword', None)
    max_price = request.GET.get('max_price', None)
    min_price = request.GET.get('min_price', None)
    beds = request.GET.get('beds', None)
    bedrooms = request.GET.get('bedrooms', None)
    bathrooms = request.GET.get('bathrooms', None)
    lat = request.GET.get("lat", None)
    lng = request.GET.get("lng", None)
    filter_kwargs = {}
    if keyword is not None:
      filter_kwargs["name__icontains"] = keyword
    if max_price is not None:
      filter_kwargs["price__lte"] = max_price
    if min_price is not None:
      filter_kwargs["price__gte"] = min_price
    if beds is not None:
      filter_kwargs["beds__gte"] = beds
    if bedrooms is not None:
      filter_kwargs["bedrooms__gte"] = bedrooms
    if bathrooms is not None:
      filter_kwargs["bathrooms__gte"] = bathrooms
    if lat is not None and lng is not None:
      filter_kwargs["lat__gte"] = float(lat) - 0.005
      filter_kwargs["lat__lte"] = float(lat) + 0.005
      filter_kwargs["lng__gte"] = float(lng) - 0.005
      filter_kwargs["lng__lte"] = float(lng) + 0.005

    paginator = self.paginator
    try:
      rooms = Room.objects.filter(**filter_kwargs)
    except ValueError:
      rooms = Room.objects.all()
    results = paginator.paginate_queryset(rooms, request)
    serializer = RoomSerializer(results, many=True, context={"request":request}).data
    return paginator.get_paginated_response(serializer)
