#!/bin/bash

###########################################################
#
# OpenCV 3.0.0 - install
# http://opencv.org/
# Credit Rodrigo Berriel
# http://rodrigoberriel.com/2014/10/installing-opencv-3-0-0-on-ubuntu-14-04/
###########################################################

dateformat="+%a %b %-eth %Y %I:%M:%S %p %Z"
starttime=$(date "$dateformat")
starttimesec=$(date +%s)


curdir=$(cd `dirname $0` && pwd)

# create install log
logfile="$curdir/install-opencv.log"
rm -f $logfile

# Logger
log(){
	timestamp=$(date +"%Y-%m-%d %k:%M:%S")
	echo "\n$timestamp $1"
	echo "$timestamp $1" >> $logfile 2>&1
}

# Initiate installation of OpenCV 3.0.0
log "Initiate installation of OpenCV 3.0.0"


#----------------------------------------------------------
# Ensuring environment is upgraded
#----------------------------------------------------------

# Infrom user that apt-get is being updated
log "Execute apt-get update and apt-get upgrade"

# Performs update
sudo apt-get update
sudo apt-get upgrade


#----------------------------------------------------------
# Installing Package Dependencies
#----------------------------------------------------------

log "Installing dependencies"

# Execute
sudo apt-get -y install libopencv-dev build-essential cmake git libgtk2.0-dev pkg-config python-dev python-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff4-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev libtbb-dev libqt4-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils python-tk python-imaging-tk python-setuptools unzip


#----------------------------------------------------------
# Installing OpenCV
#----------------------------------------------------------

log "Downloading OpenCV 3.0.0"

# Define constant
FOLDER_NAME="opencv"

# Create a new directory to store the source code
mkdir ${FOLDER_NAME}

# Enter the Directory
cd ${FOLDER_NAME}

# Downloading opencv 3.0
wget https://github.com/Itseez/opencv/archive/3.0.0.zip -O opencv-3.0.0.zip

# Extracting opencv
unzip opencv-3.0.0.zip

log "Installing OpenCV 3.0.0"

# Enter Directory
cd opencv-3.0.0

# Creating 'build' directory
mkdir build

# Enter 'build' directory
cd build

# Constucting project using CMake
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..

# Compiling project
make

# Installing libraries
sudo make install

# Adds the path of OpenCV libraries to the library search paths of Ubuntu
sudo /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'

# Updates the search paths of the Ubuntu standard library
sudo ldconfig

log "OpenCV 3.0.0 was sucessfully installed!"

#----------------------------------------------------------
# Shows time spent on installation
#----------------------------------------------------------

# Done
endtime=$(date "$dateformat")
endtimesec=$(date +%s)

# Shows time spent on installation
elapsedtimesec=$(expr $endtimesec - $starttimesec)
ds=$((elapsedtimesec % 60))
dm=$(((elapsedtimesec / 60) % 60))
dh=$((elapsedtimesec / 3600))
displaytime=$(printf "%02d:%02d:%02d" $dh $dm $ds)
log "Tempo gasto: $displaytime\n"
