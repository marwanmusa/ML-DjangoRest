from .apps import *
from rest_framework.response import Response


from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .detection import get_face
from .serializers import *

class FaceRecognitionViewSet(viewsets.ModelViewSet):
    queryset = FaceRecognition.objects.all()
    serializer_class = FaceRecognitionSerializer

    def get_serializer_class(self):
        if self.action == 'detect_faces':
            return FaceRecognitionSerializer
        else:
            return super().get_serializer_class()

    @action(methods=['post'], detail=False)
    def detect_faces(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        device = serializer.validated_data['device']
        ip_address = serializer.validated_data['ip_address']

        res = get_face()[0]
        detection = {
            'Face name' : res,
            }
        FaceRecognition.objects.create(name=get_face()[0],
                                        device=device,
                                        ip_address=ip_address)
        return Response(detection, status=200)