from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import ReviewSerializer
from .models import Review
from .forms import CreateReviewForm

# Create your views here.


class ReviewViewSet(ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer

  def get_permissions(self):
    if self.action == 'list' or self.action == "retrieve":
      permission_classes = [AllowAny]
    else:
      permission_classes = [IsAuthenticated]
    return [permission() for permission in permission_classes]
