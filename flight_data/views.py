from django.shortcuts import render, redirect
from django.db import transaction  # Ensures atomicity
from .models import FlightData, FlightObservation, OtherInformation
from .forms import FlightDataForm, FlightObservationForm, OtherInformationForm

def flight_data_list(request):
    if request.method == 'POST':
        flight_data_form = FlightDataForm(request.POST)
        flight_observation_form = FlightObservationForm(request.POST)
        other_info_form = OtherInformationForm(request.POST)

        if (
            flight_data_form.is_valid() 
            and flight_observation_form.is_valid() 
            and other_info_form.is_valid()
        ):
            try:
                with transaction.atomic():
                    flight_data = flight_data_form.save()
                    
                    flight_observation = flight_observation_form.save(commit=False)
                    flight_observation.flight_data = flight_data
                    flight_observation.save()

                    other_info = other_info_form.save(commit=False)
                    other_info.flight_data = flight_data
                    other_info.save()

                return redirect('success')  # Ensure 'success' exists in urls.py
            except Exception as e:
                print(f"Error: {e}")  # Log error for debugging

    else:
        flight_data_form = FlightDataForm()
        flight_observation_form = FlightObservationForm()
        other_info_form = OtherInformationForm()

    context = {
        'flight_data_form': flight_data_form,
        'flight_observation_form': flight_observation_form,
        'other_info_form': other_info_form,
    }

    return render(request, 'flight_data/flight_data_list.html', context)
