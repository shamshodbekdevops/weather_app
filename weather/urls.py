from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_weather, name='current_weather'),
    path('pollution/', views.air_pollution, name='air_pollution'),
    path('forecast/', views.five_day_forecast, name='five_day_forecast'),
]