from django.urls import path
from .views import SensorMeasurementView, SensorUpdateView, MeasurementCreateView



urlpatterns = [

    path('sensors/', SensorMeasurementView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),

]
