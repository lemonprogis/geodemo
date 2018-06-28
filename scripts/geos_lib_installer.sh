#!/bin/bash

# Compile/install GEOS. Taken from:
# http://grasswiki.osgeo.org/wiki/Compile_and_Install_Ubuntu#GEOS_2

cd /tmp
wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
bunzip2 geos-3.4.2.tar.bz2
tar xvf  geos-3.4.2.tar

cd geos-3.4.2

./configure  &&  make  &&  sudo make install
sudo ldconfig

##########################################

# Compile & install proj.4. Taken from:
# http://grasswiki.osgeo.org/wiki/Compile_and_Install_Ubuntu#PROJ4

sudo apt-get install subversion

cd /tmp
svn co http://svn.osgeo.org/metacrs/proj/branches/4.8/proj/

cd /tmp/proj/nad
sudo wget http://download.osgeo.org/proj/proj-datumgrid-1.5.zip

unzip -o -q proj-datumgrid-1.5.zip

#make distclean

cd /tmp/proj/

./configure  &&  make  &&  sudo make install && sudo ldconfig

##########################################

# install gdal 1.10.1 - must happen after proj & geos
# taken from:
# http://grasswiki.osgeo.org/wiki/Compile_and_Install_Ubuntu#GDAL

# sudo apt-get install libtiff4

cd /tmp
svn co https://svn.osgeo.org/gdal/branches/1.10/gdal gdal_stable
cd gdal_stable
#make distclean
CFLAGS="-g -Wall" LDFLAGS="-s" ./configure \
	--with-png=internal \
	--with-libtiff=internal \
	--with-geotiff=internal \
	--with-jpeg=internal \
	--with-gif=internal \
	--with-ecw=no \
	--with-expat=yes \
	--with-sqlite3=yes \
	--with-geos=yes \
	--with-python \
	--with-libz=internal \
	--with-netcdf \
	--with-threads=yes \
	--without-grass  \
	--without-ogdi \
	--with-xerces=yes

#with-pg=/usr/bin/pg_config \

	make -j2  &&  sudo make install  &&  sudo ldconfig
