from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_data_list, name='flight-data-list'),  # For the HTML page
    path('success/', lambda request: render(request, 'flight_data/success.html'), name='success'),
]