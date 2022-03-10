from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "photo_number",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.HouseRule)
class HouseRuleAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass