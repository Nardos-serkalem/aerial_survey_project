from django.urls import path
from . import api_views

urlpatterns = [
    path('flight_data/', api_views.FlightDataList.as_view(), name='flight-data-list-api'), # For the API
]