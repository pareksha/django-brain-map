from django.urls import path
from api.views import *

urlpatterns = [
    path('predict/digit/<int:digit>/', PredictDigit.as_view()),
]