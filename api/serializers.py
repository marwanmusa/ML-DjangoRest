import socket
# from .detection import get_face
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

hostname = socket.gethostname()
ip_add = socket.gethostbyname(hostname)


class FaceRecognitionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, default='unknown')
    device = serializers.CharField(max_length=255,  default=hostname)
    ip_address = serializers.CharField(max_length=255, default=ip_add)

    class Meta:
        model = FaceRecognition
        fields = '__all__'