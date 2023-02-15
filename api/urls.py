from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(prefix='face-recognition', viewset=FaceRecognitionViewSet)

urlpatterns = [
    # path('weight-prediction/<int:pk>', WeightPredictionDetail.as_view(), name='body-detail'),
]
urlpatterns += router.urls
