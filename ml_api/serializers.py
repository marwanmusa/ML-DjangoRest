from rest_framework import serializers
from .models import *

class WeightPredictionSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(WeightPrediction.group_gender, required=True)
    height = serializers.IntegerField()

    class Meta:
        model = WeightPrediction
        fields = '__all__'