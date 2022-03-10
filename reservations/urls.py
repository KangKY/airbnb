from rest_framework.routers import DefaultRouter
from . import views

app_name = 'reservations'
router = DefaultRouter()
router.register("", views.ReservationViewSet)

urlpatterns = router.urls