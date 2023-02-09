from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    data = serializers.PrimaryKeyRelatedField(many=True, queryset=WeightPrediction.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = User
        fields = ['id', 'username', 'data', 'owner']


class WeightPredictionSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(WeightPrediction.group_gender, required=True)
    height = serializers.IntegerField()

    class Meta:
        model = WeightPrediction
        fields = '__all__'