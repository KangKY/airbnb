from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
  """ Conversation Admin Definition """

  list_display = (
    "id",
  )

  #list_filter = ("status",)


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = ("message", "user")