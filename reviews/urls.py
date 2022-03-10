from rest_framework.routers import DefaultRouter
from . import views

app_name = 'reivews'
router = DefaultRouter()
router.register("", views.ReviewViewSet)

urlpatterns = router.urls