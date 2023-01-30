import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response

class Prediction(APIView):
    def post(self, request):
        age = request.GET.get('age')
        gender = request.GET.get('gender')
        bp = request.GET.get('bp')
        cholesterol = request.GET.get('cholesterol')
        salt = request.GET.get('salt')
        dtree = ModelDTree.model

        # predict using independent variable
        get_prediction = dtree.predict([[age, gender, cholesterol, bp, salt]])
        res = {"Predicted drug": get_prediction}
        print(res)
        return Response(res, status=200)