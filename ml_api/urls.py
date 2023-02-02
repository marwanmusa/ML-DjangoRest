from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(prefix='weight-prediction', viewset = WeightPredictionViewSet)

urlpatterns = router.urls