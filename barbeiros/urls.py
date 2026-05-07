from rest_framework import routers
from .views import BarbeiroViewSet

router = routers.DefaultRouter()
router.register(r'', BarbeiroViewSet)
urlpatterns = router.urls
