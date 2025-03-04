from django.db import models

class FlightData(models.Model):
    project_name = models.CharField(max_length=255, blank=True, null=True)
    block_number = models.CharField(max_length=255, blank=True, null=True)
    flight_number = models.CharField(max_length=255, blank=True, null=True)
    flight_date = models.DateField(blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    pilot = models.CharField(max_length=255, blank=True, null=True)
    departure = models.CharField(max_length=255, blank=True, null=True)
    overlap = models.FloatField(blank=True, null=True)
    gsd = models.FloatField(blank=True, null=True)
    aircraft = models.CharField(max_length=255, blank=True, null=True)
    navigation_system = models.CharField(max_length=255, blank=True, null=True)
    mount = models.CharField(max_length=255, blank=True, null=True)
    imu = models.CharField(max_length=255, blank=True, null=True)
    camera = models.CharField(max_length=255, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    focal_length = models.FloatField(blank=True, null=True)
    gps_data_logging_time = models.TimeField(blank=True, null=True)
    sun_angle = models.FloatField(blank=True, null=True)
    internal_pos_data_code = models.CharField(max_length=255, blank=True, null=True)
    aperture = models.FloatField(blank=True, null=True)
    shutter_speed = models.FloatField(blank=True, null=True)
    iso = models.IntegerField(blank=True, null=True)
    fmc = models.FloatField(blank=True, null=True)
    ibd = models.FloatField(blank=True, null=True)
    engine_start = models.TimeField(blank=True, null=True)
    start_movement = models.TimeField(blank=True, null=True)
    take_off = models.TimeField(blank=True, null=True)
    landing = models.TimeField(blank=True, null=True)
    stop_movement = models.TimeField(blank=True, null=True)
    shutdown = models.TimeField(blank=True, null=True)
    weather = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Flight {self.flight_number} on {self.flight_date}"


class FlightRunData(models.Model):
    flight_data = models.ForeignKey(FlightData, on_delete=models.CASCADE, related_name='flight_runs')
    time_of_entry = models.TimeField(blank=True, null=True)
    time_of_end = models.TimeField(blank=True, null=True)
    turning_time = models.FloatField(blank=True, null=True)
    run_number = models.IntegerField(blank=True, null=True)
    heading = models.FloatField(blank=True, null=True)
    direction = models.CharField(max_length=10, blank=True, null=True)
    photo_numbers = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    run_remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Run {self.run_number} for Flight {self.flight_data.flight_number}"