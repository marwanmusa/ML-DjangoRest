from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'


# class FaceRecognitionConfig(AppConfig):
#     name = 'face_recognition_agent'
#     model = get_face()
