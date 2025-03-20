from django.contrib import admin
from .models import FlightData, FlightObservation, OtherInformation

admin.site.register(FlightData)
admin.site.register(FlightObservation)
admin.site.register(OtherInformation)

