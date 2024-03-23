from rest_framework import routers

from cardapp.rest_views import (
  CardViewSet
)

router = routers.DefaultRouter()

app_name = 'cardapp'

router.register('cards', CardViewSet)

urlpatterns = router.urls