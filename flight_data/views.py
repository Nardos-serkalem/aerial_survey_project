from django.shortcuts import render
from .models import FlightData

def flight_data_list(request):
    if request.method == 'POST':
        # Retrieve data from the form
        project_name = request.POST.get('project_name')
        pilot = request.POST.get('pilot')
        flight_date = request.POST.get('flight_date')
        flight_no_day = request.POST.get('flight_no_day')
        departure = request.POST.get('departure')
        overlap = request.POST.get('overlap')
        gsd = request.POST.get('gsd')
        aircraft = request.POST.get('aircraft')
        navigation_system = request.POST.get('navigation_system')
        mount = request.POST.get('mount')
        imu = request.POST.get('imu')
        camera = request.POST.get('camera')
        serial_no = request.POST.get('serial no')
        focal_length = request.POST.get('focal length')
        gps_data_logging_time = request.POST.get('gps_data_logging_time')
        sun_angle = request.POST.get('sun angle')
        none = request.POST.get('none ')
        internal_pos_data_code = request.POST.get('internal_pos_data_code')
        aperture = request.POST.get('aperture')
        shutter_speed = request.POST.get('shutter speed')
        iso = request.POST.get('iso')
        fmc = request.POST.get('fmc')
        ibd = request.POST.get('ibd')
        engine_start = request.POST.get('engine_start')
        start_movement = request.POST.get('start_movement')
        take_off = request.POST.get('take off')
        landing = request.POST.get('landing')
        stop_movement = request.POST.get('stop_movement')
        shutdown = request.POST.get('shutdown')
        time_of_entry = request.POST.get('time_of_entry')
        time_of_end = request.POST.get('time_of_end')
        turning_time = request.POST.get('turning_time')
        run = request.POST.get('run')
        heading = request.POST.get('heading')
        dir = request.POST.get('dir')
        photo_numbers = request.POST.get('photo_numbers')
        qty = request.POST.get('qty')
        remarks = request.POST.get('remarks')
        weather = request.POST.get('weather')
        remarks_textarea = request.POST.get('remarks')  # Corrected name
        signature = request.POST.get('signature')

        # Create a FlightData instance and save it to the database
        flight_data = FlightData(
            project_name=project_name,
            pilot=pilot,
            flight_date=flight_date,
            flight_no_day=flight_no_day,
            departure=departure,
            overlap=overlap,
            gsd=gsd,
            aircraft=aircraft,
            navigation_system=navigation_system,
            mount=mount,
            imu=imu,
            camera=camera,
            serial_no=serial_no,
            focal_length=focal_length,
            gps_data_logging_time=gps_data_logging_time,
            sun_angle=sun_angle,
            none=none,
            internal_pos_data_code=internal_pos_data_code,
            aperture=aperture,
            shutter_speed=shutter_speed,
            iso=iso,
            fmc=fmc,
            ibd=ibd,
            engine_start=engine_start,
            start_movement=start_movement,
            take_off=take_off,
            landing=landing,
            stop_movement=stop_movement,
            shutdown=shutdown,
        )
        flight_data.save()

        # Create context for results.html
        context = {
            'project_name': project_name,
            'pilot': pilot,
            'flight_date': flight_date,
            'flight_no_day': flight_no_day,
            'departure': departure,
            'overlap': overlap,
            'gsd': gsd,
            'aircraft': aircraft,
            'navigation_system': navigation_system,
            'mount': mount,
            'imu': imu,
            'camera': camera,
            'serial_no': serial_no,
            'focal_length': focal_length,
            'gps_data_logging_time': gps_data_logging_time,
            'sun_angle': sun_angle,
            'none': none,
            'internal_pos_data_code': internal_pos_data_code,
            'aperture': aperture,
            'shutter_speed': shutter_speed,
            'iso': iso,
            'fmc': fmc,
            'ibd': ibd,
            'engine_start': engine_start,
            'start_movement': start_movement,
            'take_off': take_off,
            'landing': landing,
            'stop_movement': stop_movement,
            'shutdown': shutdown,
            'time_of_entry': time_of_entry,
            'time_of_end': time_of_end,
            'turning_time': turning_time,
            'run': run,
            'heading': heading,
            'dir': dir,
            'photo_numbers': photo_numbers,
            'qty': qty,
            'remarks': remarks,
            'weather': weather,
            'remarks_textarea': remarks_textarea,
            'signature': signature,
        }

        # Render results.html with the context
        return render(request, 'flight_data/results.html', context)

    else:
        # Display the form (GET request)
        flight_data = FlightData.objects.all()
        return render(request, 'flight_data/flight_data_list.html', {'flight_data': flight_data})