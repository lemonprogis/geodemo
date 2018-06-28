# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class WeatherStation(models.Model):
    '''
        ~bash$ ogrinfo -so data/NOAA_stations.shp NOAA_stations
            INFO: Open of `data/NOAA_stations.shp'
                  using driver `ESRI Shapefile' successful.

            Layer name: NOAA_stations
            Metadata:
              DBF_DATE_LAST_UPDATE=2010-08-06
            Geometry: Point
            Feature Count: 29567
            Extent: (-180.000000, -90.000000) - (179.750000, 89.383000)
            Layer SRS WKT:
            GEOGCS["GCS_WGS_1984",
                DATUM["WGS_1984",
                    SPHEROID["WGS_84",6378137.0,298.257223563]],
                PRIMEM["Greenwich",0.0],
                UNIT["Degree",0.0174532925199433],
                AUTHORITY["EPSG","4326"]]
            OBJECTID: Integer (9.0)
            USAF: Real (19.11)
            WBAN: Real (19.11)
            STATION_NA: String (254.0)
            CTRY: String (254.0)
            ST: String (254.0)
            CALL: String (254.0)
            LAT: Real (19.11)
            LON: Real (19.11)
            ELEV: Real (19.11)
    '''
    objectid = models.IntegerField(null=True)
    usaf = models.FloatField()
    wban = models.FloatField()
    station_na = models.CharField(max_length=254)
    ctry = models.CharField(max_length=254)
    st = models.CharField(max_length=254)
    call = models.CharField(max_length=254)
    lat = models.FloatField()
    lon = models.FloatField()
    elev = models.FloatField()
    mpoint = models.MultiPointField(srid=4326)

    # Returns the string representation of the model.
    def __str__(self):
        return self.station_na

class WorldBorderSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = WorldBorder
        geo_field = "mpoint"
        fields = ('fips','iso2','iso3','un','name','area','pop2005','region','subregion','lon','lat')

class WeatherStationSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = WeatherStation
        geo_field = 'mpoint'
        fields = ('usaf', 'wban', 'station_na', 'ctry', 'st', 'call', 'lat', 'lon', 'elev')