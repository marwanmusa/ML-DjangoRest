from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(prefix='predictions', viewset=PredictionViewSet)

urlpatterns = router.urls