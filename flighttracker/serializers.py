from rest_framework import serializers

from flighttracker.models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Passenger
        fields = ['id', 'first_name', 'last_name', 'flight_points']

