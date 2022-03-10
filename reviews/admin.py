from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
  """ Review Admin Definition """

  list_display = (
    "user",
    "room",
    "review",
    "value",
    "rating_average",
  )
