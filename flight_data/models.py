from django.db import models

class FlightData(models.Model):
    flight_number = models.CharField(max_length=255, blank=True, null=True)
    flight_date = models.DateField(blank=True, null=True)
    # ... other fields ...
    weather = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Flight {self.flight_number} on {self.flight_date}"