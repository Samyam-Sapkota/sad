from django.shortcuts import render
from django.http import JsonResponse
from .models import Vehicle

def get_latest_location(request):
    vehicle = Vehicle.objects.first()
    data = {
        'latitude': vehicle.latitude,
        'longitude': vehicle.longitude,
    }
    return JsonResponse(data)


def index(request):
    return render(request, 'index.html')
