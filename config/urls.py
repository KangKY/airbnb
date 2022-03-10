from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("admin/", admin.site.urls),
  path("api/v1/rooms/", include("rooms.urls")),
  path("api/v1/users/", include("users.urls")),
  path("api/v1/reservations/", include("reservations.urls")),
  path("api/v1/reviews/", include("reviews.urls")),
  path("api/v1/conversations/", include("conversations.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
