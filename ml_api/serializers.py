from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create_user(**validated_data)
        return user


class WeightPredictionSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(WeightPrediction.group_gender, required=True)
    height = serializers.IntegerField()

    class Meta:
        model = WeightPrediction
        fields = '__all__'