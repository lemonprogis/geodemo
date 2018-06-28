# demo command line calls

ogrinfo /home/lemonpro/geodjango-presentation/data/TM_WORLD_BORDERS-0.3.shp

# get more info about our shapefile
ogrinfo -so /home/lemonpro/geodjango-presentation/data/TM_WORLD_BORDERS-0.3.shp

# generates mappings and layer definition
python manage.py ogrinspect /home/lemonpro/geodjango-presentation/data/TM_WORLD_BORDERS-0.3.shp WorldBorder --srid=4326 --mapping --multi