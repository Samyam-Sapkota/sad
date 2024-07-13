from django.core.management.base import BaseCommand
from tracking.models import Vehicle
import time
import random

class Command(BaseCommand):
    help = 'Simulate GPS data for a vehicle'

    def handle(self, *args, **kwargs):
        # Provide initial values for latitude and longitude
        vehicle, created = Vehicle.objects.get_or_create(name='Sajha', defaults={'latitude': 27.674792596386062, 'longitude': 85.35872295031606})
        
        while True:
            # Update vehicle location with random small changes
            vehicle.latitude += random.uniform(-0.0001, 0.0001)
            vehicle.longitude += random.uniform(-0.0001, 0.0001)
            vehicle.save()
            self.stdout.write(self.style.SUCCESS(f'Updated location: {vehicle.latitude}, {vehicle.longitude}'))
            time.sleep(2)  # Update every 2 seconds






