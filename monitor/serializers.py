from rest_framework import serializers
from .models import *

class PredictionSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(Prediction.group_sex, required=True)
    bp = serializers.ChoiceField(Prediction.group_bp, required=True)
    cholesterol = serializers.ChoiceField(Prediction.group_chol, required=True)
    salt = serializers.FloatField()
    
    class Meta:
        model = Prediction
        fields = '__all__'