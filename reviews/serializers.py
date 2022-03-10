from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializer
from users.models import User


class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = (
      'id',
      'review',
      'accuracy',
      'communication',
      'cleanliness',
      'location',
      'check_in',
      'value',
      'user',
      'room',
      'rating_average'
    )

    read_only_fields = ("user", "id", "rating_average", "created", "updated")

  def create(self, validated_data):
    request =  self.context.get("request")
    review = Review.objects.create(**validated_data, user=request.user)
    return review
