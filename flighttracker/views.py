from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from flighttracker.models import Passenger
from flighttracker.serializers import PassengerSerializer

@api_view(['GET', 'POST'])
def passenger_list(request):
    if request.method == 'GET':
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(Serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PassengerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def passenger_detail(request, pk):
    try:
        passenger = Passenger.objects.get(id=pk)
    except Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PassengerSerializer(passenger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


