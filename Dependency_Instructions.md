
# Install Instructions for Linux System

This was tested on the following Linux Systems:

* Ubuntu
* Raspbian

## OpenCV Install OpenCV 3.0 with Python 2.7+ Ubuntu
NOTE: Install Instructions [Source](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/)

#### Apply Update to System

```$ sudo apt-get update```

```$ sudo apt-get upgrade```

#### Install Developer Tools

```$ sudo apt-get install build-essential cmake git pkg-config```

#### Install I/O Packages for Reading Files

```$ sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev```

#### Install GUI Interface Prackage

```$ sudo apt-get install libgtk2.0-dev```

#### Install Video Stream Packages

```$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev```

#### Install Optimization Libraries

```$ sudo apt-get install libatlas-base-dev gfortran```

#### Install Python Package Manager Pip

```$ wget https://bootstrap.pypa.io/get-pip.py```

```$ sudo python get-pip.py```

#### Install Python 2.7+ Development Tools

```$ sudo apt-get install python2.7-dev```

#### Install NumPy

```$ pip install numpy```

#### Pull Code from OpenCV Repository into Home Directory

```
$ cd ~ 
$ git clone https://github.com/Itseez/opencv.git
$ cd opencv
$ git checkout 3.0.0
```

#### Pull Extra OpenCV Libraries

```
$ cd ~
$ git clone https://github.com/Itseez/opencv_contrib.git
$ cd opencv_contrib
$ git checkout 3.0.0
```

#### Build OpenCV
```
$ cd ~/opencv
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..
```

#### Make OpenCV

```$ make ```

#### Install OpenCV

```$ sudo make install```

```$ sudo ldconfig```

#### Verify Install

Start Python

```$ python ```

Import OpenCV

```> import cv2 ```

Check Version

```> cv2.__version__ ```

Verify the Response is: *'3.0.0'*

**To Exit the Python Interpreter Type: ``` exit() ```**
