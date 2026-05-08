from rest_framework import routers
from .views import AgendamentoViewSet

router = routers.DefaultRouter()
router.register(r'', AgendamentoViewSet)
urlpatterns = router.urls