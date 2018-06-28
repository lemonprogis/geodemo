from django.shortcuts import render
from .models import *
from django.core import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_world_borders(request):
	data = WorldBorder.objects.all()
	serializer = WorldBorderSerializer(data, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def get_weather_stations(request):
	pass
	data = WeatherStation.objects.all()
	serializer = WeatherStationSerializer(data, many=True)
	return Response(serializer.data)

def index(request):
	return render(request, 'viewer/index.html', {})