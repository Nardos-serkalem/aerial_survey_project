from django.db import models
from datetime import time  # Import time from datetime

class FlightData(models.Model):
    project_name = models.CharField(max_length=255, verbose_name="Project Name & Block No.")
    flight_no_day = models.CharField(max_length=255, verbose_name="Flight No. Day")
    operators = models.CharField(max_length=255)
    pilot = models.CharField(max_length=255)
    flight_date = models.DateField()
    departure = models.CharField(max_length=255)
    overlap = models.FloatField(verbose_name="Overlap (%)")
    gsd = models.CharField(max_length=255, verbose_name="GSD (cm)")
    aircraft = models.CharField(max_length=255, default="Unknown")
    navigation_system = models.CharField(max_length=255, default="Unknown")
    mount = models.CharField(max_length=255, default="Unknown")
    imu = models.CharField(max_length=255, default="Unknown")
    camera = models.CharField(max_length=255, default="Unknown")
    serial_no = models.CharField(max_length=255, verbose_name="Serial No")
    focal_length = models.CharField(max_length=255, default="Unknown")
    gps_data_logging_time = models.TimeField(null=True, blank=True, verbose_name="GPS Data Logging Time", default=time(0, 0))
    sun_angle = models.CharField(max_length=255, verbose_name="Sun Angle", default="Unknown")
    none = models.CharField(max_length=255, default="None")  # Consider renaming this
    internal_pos_data_code = models.CharField(max_length=255, default="Unknown")
    aperture = models.CharField(max_length=255, default="Unknown")
    shutter_speed = models.CharField(max_length=255, default="Unknown")
    iso = models.CharField(max_length=255, default="Unknown")
    fmc = models.CharField(max_length=255, default="Unknown")
    ibd = models.CharField(max_length=255, default="Unknown")
    engine_start = models.TimeField(null=True, blank=True, verbose_name="Engine Start", default=time(0, 0))
    start_movement = models.TimeField(null=True, blank=True, verbose_name="Start Movement", default=time(0, 0))
    take_off = models.CharField(max_length=255, verbose_name="Take off", default="Unknown")
    landing = models.TimeField(null=True, blank=True, verbose_name="Landing", default=time(0, 0))
    stop_movement = models.TimeField(null=True, blank=True, verbose_name="Stop Movement", default=time(0, 0))
    shutdown = models.CharField(max_length=255, verbose_name="Shutdown", default="Unknown")

    def __str__(self):
        return self.project_name + " - " + str(self.flight_date)

class FlightObservation(models.Model):
    flight_data = models.ForeignKey(FlightData, on_delete=models.CASCADE, related_name='observations')
    time_of_entry = models.TimeField()
    time_of_end = models.TimeField(null=True, blank=True, default=time(0, 0))
    turning_time = models.IntegerField(null=True, blank=True, verbose_name="Turning Time")
    run = models.IntegerField(null=True, blank=True)
    heading = models.IntegerField(null=True, blank=True)
    dir = models.CharField(max_length=50, verbose_name="Dir.")
    photo_numbers = models.CharField(max_length=255, verbose_name="Photo Numbers")
    qty = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.time_of_entry) + " - " + str(self.time_of_end)

class OtherInformation(models.Model):
    flight_data = models.OneToOneField(FlightData, on_delete=models.CASCADE, related_name='other_info')
    weather = models.CharField(max_length=255, blank=True)
    remarks = models.TextField(blank=True)
    signature = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "Other Info for " + str(self.flight_data)