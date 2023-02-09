import os
import joblib
from django.apps import AppConfig
from django.conf import settings

class MlAgentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ml_agent'


class ModelLinReg(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "WeightPredictionLinRegModel.joblib")
    model = joblib.load(MODEL_FILE)