from rest_framework.routers import SimpleRouter

from .views import PropostasViewSet

router = SimpleRouter()
router.register('propostas', PropostasViewSet, basename='proposta')