import os
from django.contrib.gis.utils import LayerMapping
from .models import WeatherStation

weatherstation_mapping = {
    'objectid' : 'OBJECTID',
    'usaf' : 'USAF',
    'wban' : 'WBAN',
    'station_na' : 'STATION_NA',
    'ctry' : 'CTRY',
    'st' : 'ST',
    'call' : 'CALL',
    'lat' : 'LAT',
    'lon' : 'LON',
    'elev' : 'ELEV',
    'mpoint' : 'MULTIPOINT',
}

weatherstation_shp = '/home/lemonpro/apps/geodjango-presentation/data/NOAA_stations.shp'

def run(verbose=True):
    lm = LayerMapping(
        WeatherStation, weatherstation_shp, weatherstation_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)