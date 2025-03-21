from django import forms
from .models import FlightData, FlightObservation, OtherInformation
from datetime import time

class FlightDataForm(forms.ModelForm):
    class Meta:
        model = FlightData
        fields = [
            'project_name', 'flight_no_day', 'operators', 'pilot', 'flight_date', 'departure',
            'overlap', 'gsd', 'aircraft', 'navigation_system', 'mount', 'imu', 'camera',
            'serial_no', 'focal_length', 'gps_data_logging_time', 'sun_angle', 'none_type',
            'internal_pos_data_code', 'aperture', 'shutter_speed', 'iso', 'fmc', 'ibd',
            'engine_start', 'start_movement', 'take_off', 'landing', 'stop_movement', 'shutdown'
        ]
        widgets = {
            'flight_date': forms.DateInput(attrs={'type': 'date'}),
            'gps_data_logging_time': forms.TimeInput(attrs={'type': 'time'}),
            'engine_start': forms.TimeInput(attrs={'type': 'time'}),
            'start_movement': forms.TimeInput(attrs={'type': 'time'}),
            'landing': forms.TimeInput(attrs={'type': 'time'}),
            'stop_movement': forms.TimeInput(attrs={'type': 'time'}),
        }

class FlightObservationForm(forms.ModelForm):
    class Meta:
        model = FlightObservation
        fields = [
            'flight_data', 'time_of_entry', 'time_of_end', 'turning_time', 'run', 'heading', 
            'direction', 'photo_numbers', 'qty', 'remarks'
        ]
        widgets = {
            'time_of_entry': forms.TimeInput(attrs={'type': 'time'}),
            'time_of_end': forms.TimeInput(attrs={'type': 'time'}),
        }

class OtherInformationForm(forms.ModelForm):
    class Meta:
        model = OtherInformation
        fields = ['weather', 'remarks', 'signature']
