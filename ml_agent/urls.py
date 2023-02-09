from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import *

router = routers.DefaultRouter()
router.register(prefix='users', viewset=UserViewSet)
router.register(prefix='weight-prediction', viewset=WeightPredictionViewSet)

urlpatterns = [
    # path('weight-prediction/<int:pk>', WeightPredictionDetail.as_view(), name='body-detail'),
]
urlpatterns += router.urls
