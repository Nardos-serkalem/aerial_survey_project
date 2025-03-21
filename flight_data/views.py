# flight_data/views.py

from django.shortcuts import render
from .forms import FlightDataForm  # Import your form
from .models import FlightData  # Import your model

def flight_data_list(request):
    flight_data = None  # Ensure the variable is always defined
    
    if request.method == 'POST':
        form = FlightDataForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            # Save the data to the database (if needed)
            flight_data = form.save()

            # Pass the data to the template to display it
            context = {
                'project_name': flight_data.project_name,
                'flight_no_day': flight_data.flight_no_day,
                'flight_date': flight_data.flight_date,
                'departure': flight_data.departure,
                'overlap': flight_data.overlap,
                'gsd': flight_data.gsd,
                'aircraft': flight_data.aircraft,
                'navigation_system': flight_data.navigation_system,
                'mount': flight_data.mount,
                'imu': flight_data.imu,
                'camera': flight_data.camera,
                'serial_no': flight_data.serial_no,
                'focal_length': flight_data.focal_length,
                'gps_data_logging_time': flight_data.gps_data_logging_time,
                'sun_angle': flight_data.sun_angle,
                'internal_pos_data_code': flight_data.internal_pos_data_code,
                'aperture': flight_data.aperture,
                'shutter_speed': flight_data.shutter_speed,
                'iso': flight_data.iso,
                'fmc': flight_data.fmc,
                'ibd': flight_data.ibd,
                'engine_start': flight_data.engine_start,
                'start_movement': flight_data.start_movement,
                'take_off': flight_data.take_off,
                'landing': flight_data.landing,
                'stop_movement': flight_data.stop_movement,
                'shutdown': flight_data.shutdown,
                'time_of_entry': flight_data.time_of_entry,
                'time_of_end': flight_data.time_of_end,
                'turning_time': flight_data.turning_time,
                'run': flight_data.run,
                'heading': flight_data.heading,
                'dir': flight_data.dir,
                'photo_numbers': flight_data.photo_numbers,
                'qty': flight_data.qty,
                'remarks': flight_data.remarks,
                'weather': flight_data.weather,
                'remarks_textarea': flight_data.remarks_textarea,
                'signature': flight_data.signature,
            }

            # Render the results template with the context data
            return render(request, 'flight_data/results.html', context)
    else:
        form = FlightDataForm()  # Empty form for GET request
    
    # Render the flight data list page even for GET requests
    return render(request, 'flight_data/flight_data_list.html', {'flight_data': flight_data, 'form': form})
