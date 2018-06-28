from django.conf.urls import url

from views import *

urlpatterns = [
	url(r'^$', index),
    url(r'^world-borders/$',get_world_borders),
    url(r'^weather-stations/$',get_weather_stations),
]