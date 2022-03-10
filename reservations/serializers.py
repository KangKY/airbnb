from rest_framework import serializers
from .models import Reservation, BookedDay

class BookedDaySerializer(serializers.ModelSerializer):
  class Meta:
    model = BookedDay
    fields = ("day")
    #fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
  booked_day = BookedDaySerializer(read_only=True, many=True)
  class Meta:
    model = Reservation
    fields = (
      "id",
      "status",
      "check_in",
      "check_out",
      "guest",
      "room",
      "booked_day",
      "in_progress",
      "is_finished"
    )

  def create(self, validated_data):
    request =  self.context.get("request")
    reservation = Reservation.objects.create(**validated_data, guest=request.user)
    return reservation

  def update(self, reservation, validated_data):
    print(validated_data)
    status = validated_data.get('status', reservation.status)
    if status == "confirm":
      reservation.status = Reservation.STATUS_CONFIRMED
    elif status == "cancel":
      reservation.status = Reservation.STATUS_CANCELED
      BookedDay.objects.filter(reservation=reservation).delete()
    elif status == "pending":
      reservation.status = Reservation.STATUS_PENDING
    
    reservation.save()
    return reservation