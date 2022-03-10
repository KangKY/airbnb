from django.db import models
from core.models import CoreModel
from django.utils import timezone
import calendar


class Day:
  def __init__(self, number, past, month, year):
      self.number = number
      self.past = past
      self.month = month
      self.year = year

  def __str__(self):
      return str(self.number)


class Calendar(calendar.Calendar):
  def __init__(self, year, month):
      super().__init__(firstweekday=6)
      self.year = year
      self.month = month
      self.day_names = ("일", "월", "화", "수", "목", "금", "토")
      self.months = (
          "1월",
          "2월",
          "3월",
          "4월",
          "5월",
          "6월",
          "7월",
          "8월",
          "9월",
          "10월",
          "11월",
          "12월",
      )

  def get_days(self):
      weeks = self.monthdays2calendar(self.year, self.month)
      days = []
      for week in weeks:
          for day, _ in week:
              now = timezone.now()
              today = now.day
              month = now.month
              past = False
              if month == self.month:
                  if day <= today:
                      past = True
              new_day = Day(number=day, past=past, month=self.month, year=self.year)
              days.append(new_day)
      return days

  def get_month(self):
      return self.months[self.month - 1]

class AbstractItem(CoreModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Room(CoreModel):

    name = models.CharField(max_length=140)
    description = models.TextField(default="")
    address = models.CharField(max_length=140)
    price = models.IntegerField(help_text="원")
    beds = models.IntegerField(default=1)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    guests = models.IntegerField(default=1, help_text="기준인원")
    #extra_guests = models.IntegerField(default=1, help_text="최대 추가인원")
    beds = models.IntegerField()
    check_in = models.TimeField(default="00:00:00")
    check_out = models.TimeField(default="00:00:00")
    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rooms"
    )

    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )

    amenities = models.ManyToManyField(
        "Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField(
        "Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(
        "HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def photo_number(self):
        return self.photos.count()

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    def first_photo(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos

    def get_calendars(self):
        now = timezone.now()
        this_year = now.year
        this_month = now.month
        next_month = this_month + 1
        if this_month == 12:
            next_month = 1
        this_month_cal = Calendar(this_year, this_month)
        next_month_cal = Calendar(this_year, next_month)
        return [this_month_cal, next_month_cal]

    photo_number.short_description = "Photo Count"

    class Meta:
      ordering = ["-pk"]


class Photo(CoreModel):

    file = models.ImageField()
    room = models.ForeignKey(
        "rooms.Room", related_name="photos", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.room.name
