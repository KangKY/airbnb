from django.db import models
from core.models import CoreModel
from django.utils.translation import gettext_lazy as _

class Conversation(CoreModel):
  """ Conversation Model Definition """
  participants = models.ManyToManyField(
    "users.User", related_name="converstation", blank=True
  )
  class Meta:
    ordering = ("-created",)
  
  def count_messages(self):
    return self.messages.count()

class Message(CoreModel):

  """ Message Model Definition """

  message = models.TextField()
  # is_read = models.BooleanField(_('active'),
  #       default=False,
  #       help_text=_(
  #           'whether this message read '
  #       ))
  user = models.ForeignKey(
      "users.User", related_name="messages", on_delete=models.CASCADE
  )
  conversation = models.ForeignKey(
      "Conversation", related_name="messages", on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.user} says: {self.message}"

  class Meta:
    ordering = ("created",)
