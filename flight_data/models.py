from django.db import models
from datetime import time

class FlightData(models.Model):
    project_name = models.CharField(max_length=255, verbose_name="Project Name & Block No.")
    flight_no_day = models.CharField(max_length=255, verbose_name="Flight No. Day")
    operators = models.CharField(max_length=255)
    pilot = models.CharField(max_length=255)
    flight_date = models.DateField()
    departure = models.CharField(max_length=255)
    overlap = models.FloatField(verbose_name="Overlap (%)")
    gsd = models.CharField(max_length=255, verbose_name="GSD (cm)")
    aircraft = models.CharField(max_length=255, default="Unknown", null=True)
    navigation_system = models.CharField(max_length=255, default="Unknown", null=True)
    mount = models.CharField(max_length=255, default="Unknown", null=True)
    imu = models.CharField(max_length=255, default="Unknown", null=True)
    camera = models.CharField(max_length=255, default="Unknown", null=True)
    serial_no = models.CharField(max_length=255, verbose_name="Serial No")
    focal_length = models.CharField(max_length=255, default="Unknown", null=True)
    gps_data_logging_time = models.TimeField(null=True, blank=True, verbose_name="GPS Data Logging Time", default=time(0, 0))
    sun_angle = models.CharField(max_length=255, verbose_name="Sun Angle", default="Unknown")
    none_type = models.CharField(max_length=255, default="None")  # Renamed 'none' to 'none_type'
    internal_pos_data_code = models.CharField(max_length=255, default="Unknown", null=True)
    aperture = models.CharField(max_length=255, default="Unknown", null=True)
    shutter_speed = models.CharField(max_length=255, default="Unknown", null=True)
    iso = models.CharField(max_length=255, default="Unknown", null=True)
    fmc = models.CharField(max_length=255, default="Unknown", null=True)
    ibd = models.CharField(max_length=255, default="Unknown", null=True)
    engine_start = models.TimeField(null=True, blank=True, verbose_name="Engine Start", default=time(0, 0))
    start_movement = models.TimeField(null=True, blank=True, verbose_name="Start Movement", default=time(0, 0))
    take_off = models.CharField(max_length=255, verbose_name="Take off", default="Unknown")
    landing = models.TimeField(null=True, blank=True, verbose_name="Landing", default=time(0, 0))
    stop_movement = models.TimeField(null=True, blank=True, verbose_name="Stop Movement", default=time(0, 0))
    shutdown = models.CharField(max_length=255, verbose_name="Shutdown", default="Unknown")

    def __str__(self):
        return f"{self.project_name} - {self.flight_date}"

class FlightObservation(models.Model):
    flight_data = models.ForeignKey(FlightData, on_delete=models.CASCADE, related_name='observations')
    time_of_entry = models.TimeField()
    time_of_end = models.TimeField(null=True, blank=True, default=time(0, 0))
    turning_time = models.IntegerField(null=True, blank=True, verbose_name="Turning Time")
    run = models.IntegerField(null=True, blank=True)
    heading = models.IntegerField(null=True, blank=True)
    direction = models.CharField(max_length=50, verbose_name="Dir.")  # Renamed 'dir' to 'direction'
    photo_numbers = models.CharField(max_length=255, verbose_name="Photo Numbers")
    qty = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.time_of_entry} - {self.time_of_end}"

class OtherInformation(models.Model):
    flight_data = models.OneToOneField(FlightData, on_delete=models.CASCADE, related_name='other_info')
    weather = models.CharField(max_length=255, blank=True)
    remarks = models.TextField(blank=True)
    signature = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Other Info for {self.flight_data}"
