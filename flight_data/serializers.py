from rest_framework import serializers
from .models import FlightData

class FlightDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightData
        fields = '__all__'  # Or specify the fields you want to include