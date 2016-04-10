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

# Iniciando a instala��o do OpenCV 3.0.0
log "Iniciando a instala��o do OpenCV 3.0.0"


#----------------------------------------------------------
# Assegurando um ambiente atualizado
#----------------------------------------------------------

# Informa ao usu�rio a pr�xima a��o
log "Execute apt-get update and apt-get upgrade"

# Executa a a��o
sudo apt-get update
sudo apt-get upgrade


#----------------------------------------------------------
# Instalando os pacotes das depend�ncias
#----------------------------------------------------------

log "Installing dependencies"

# Executeo
sudo apt-get -y install libopencv-dev build-essential cmake git libgtk2.0-dev pkg-config python-dev python-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff4-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev libtbb-dev libqt4-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils unzip


#----------------------------------------------------------
# Installing OpenCV
#----------------------------------------------------------

log "Downloading OpenCV 3.0.0"

# Defini��o de constante
FOLDER_NAME="opencv"

# Cria um novo diret�rio para armazenar o c�digo-fonte
mkdir ${FOLDER_NAME}

# Entra no diret�rio
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
make -j $(nproc)

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
