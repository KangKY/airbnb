from rest_framework.routers import DefaultRouter
from . import views

app_name = 'conversations'
router = DefaultRouter()
router.register("", views.ConversationViewSet)

urlpatterns = router.urls