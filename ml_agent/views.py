import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Prefetch
from rest_framework import generics, permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .permissions import *
from .serializers import *

linreg = ModelLinReg.model


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WeightPredictionViewSet(viewsets.ModelViewSet):
    queryset = WeightPrediction.objects.all()
    serializer_class = WeightPredictionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'get_prediction':
            return WeightPredictionSerializer
        else:
            return super().get_serializer_class()

    @action(methods=['post'], detail=False)
    def get_prediction(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        gender = serializer.validated_data['gender']
        height = serializer.validated_data['height']

        map_gender = {'Male':0, 'Female':1}

        #predict using independent variable
        get_prediction = round(linreg.predict([[map_gender[gender], height]])[0][0], 1)
        res = {
            'Gender' : gender,
            'Height' : height,
            "Predicted Weight" : get_prediction
        }
        return Response(res, status=200)

