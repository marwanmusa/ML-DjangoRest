import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import AnonymousUser
from django.db.models import Prefetch
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import *

dtree = ModelDTree.model


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer

    def get_serializer_class(self):
        if self.action == 'get_prediction':
            return PredictionSerializer
        else:
            return super().get_serializer_class()

    @action(methods=["post"], detail=False)
    def get_prediction(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        age = serializer.validated_data['age']
        gender = serializer.validated_data['gender']
        bp = serializer.validated_data['bp']
        cholesterol = serializer.validated_data['cholesterol']
        salt = serializer.validated_data['salt']

        d_sex = {'M': 1, 'F': 0}
        d_bp = {'HIGH': 0, 'LOW': 1, 'NORMAL': 2}
        d_ch = {'HIGH': 0, 'LOW': 1, 'NORMAL': 2}

        # predict using independent variable
        get_prediction = dtree.predict([[age, d_sex[gender], d_ch[cholesterol], d_bp[bp], salt]])
        res = {"Predicted drug": get_prediction}
        return Response(res, status=200)