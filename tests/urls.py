from rest_framework import routers

from tests import mocks


router = routers.DefaultRouter()

router.register(r'stuff', mocks.StuffViewSet, base_name='stuff')

router.register(r'stuff/with/(?P<param>[a-z0-9]+)/(\d+)', mocks.StuffViewSet, base_name='stuff_with_param')

urlpatterns = router.urls
