from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import FlightData
from .serializers import FlightDataSerializer

class FlightDataList(APIView):  # This is for the API (JSON data)
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        flight_data = FlightData.objects.all().order_by('-id')[:1]
        serializer = FlightDataSerializer(flight_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlightDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)