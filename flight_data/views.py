from django.shortcuts import render

def flight_data_list(request):  # This is for rendering the HTML page
    return render(request, 'flight_data/flight_data_list.html')