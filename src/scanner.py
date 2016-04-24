from findContours import FindContours
from scaleDetection import ScaleDetection
from stitch import Stitcher
from determineSkew import DetermineSkew
from scannerCamera import ScannerCamera
from jsoncreator import jsonCreator
from configcommunicator import ConfigCommunicator
import numpy as np
import cv2

def scale_calibration(scaleDetect, image, objx, objy, units):
    """
    calibrates the scale and saves to config file
    Args:
        scaleDetect (ScaleDetection):
        image: the calibration image
        objx: width of calibration object
        objy: height of calibration object
        units (string): units to use
    Returns:
        True on success, False on failure
    """
    configCom = ConfigCommunicator()

    success = scaleDetect.calibrate(image, objx, objy, units)

    dictionary = {'x_scale': str(scaleDetect.x_scale), 'y_scale': str(scaleDetect.y_scale), 'units': scaleDetect.units}

    configCom.setScale(dictionary)

    configCom.saveConfig()

    return success


def get_scale(scaleDetect):
    """
    Get the scale from the scale detection object
    Args:
        scaleDetect: scale calibration object
    Returns:
        scale
    """
    return scaleDetect.getScale()

def skew_calibration(calibImages, camera_number, scanner_camera):
    """
    Calculate skew correction values
    Args:
        calibImages
        camera_number
    Returns:
        None
    """

    scanner_camera.setSkewCorrectionValues(calibImages)

    # Config file
    configCom = ConfigCommunicator()

    configCom.setSkew(scanner_camera.skew_mtx, scanner_camera.skew_dist, scanner_camera.skew_newcameramtx, camera_number)

    configCom.saveConfig()


def skew_correction(image, camSettings):
    """
    Apply skew correction to image
    Args:
        None
    Returns:
        True on success, False on failure
    """
    return camSettings.correctSkew(image)

def stitch_images(image1, image2):
    """
    Stitch 2 images
    Args:
        image1:
        image2:
    Returns:
        stitched image
    """
    stitcher = Stitcher()
    return stitcher.stitch((image1,image2)) #correct order for images?

def find_contours(image):
    """
    Find contours on image
    Args:
        image: Image to find contours on
    Returns:
        finalContours:
        contourImage:
    """
    #findContours = FindContours()
    fd = FindContours()
    contours, hierarchy, edgeImage = fd.find_all_contours(image)
    finalContours = fd.select_contours(contours, hierarchy)

    contourImage = fd.display_drawn_contours(image,finalContours)

    return finalContours, contourImage

def export_json(contours, xscale, yscale, units):
    """
    Export the contours to JSON
    Args:
        contours:
        xscale:
        yscale:
        units:
    Returns:
        True on success, False on failure
    """
    jsonData = jsonCreator()
    jsonData.addUnits(units)
    jsonData.addContours(contours)
    jsonData.addScale(xscale, yscale)
    return jsonData.exportJson()

class Scanner:
    #Functions GUI should call:
    def scaleCalibration(self, image1, objx, objy, units):
        """
        Calibrates scale detection object and returns it
        Args:
            image1: image from camera 1 for scale detection
            objx: width of calibration object
            objy: height of calibration object
            units (string): units to use
        Returns:
            scaleDetect: ScaleDetection object needed later
        """
        #image = stitch_images(image1, image2)
        scaleDetect = ScaleDetection()
        scale_calibration(scaleDetect, image1, objx, objy, units)
        return scaleDetect #returned in order to be passed to detect_contours


    def skewCalibration(self, calibImages, camera_number):
        """
        Skew calibration. Should be run on each camera
        Args:
            calibImages: calibration images for camera 1 (any number)
            camera_number:
        Returns:
            None
        """
        scanner_camera = ScannerCamera(camera_number)
        skew_calibration(calibImages, camera_number, scanner_camera)
        return skew_correction(calibImages[0], scanner_camera)


    def processImages(self, image1):

        """
        The rest of the logic to stitch the image
        Args:
            image1: image from camera 1
        Returns:
            finalImage: image to be displayed to user to confirm it is correct
        """
        configCom = ConfigCommunicator()

        # Grabs skew info from config, and creates instance of ScannerCamera()

        skewObject = ScannerCamera(1)
        mtx, dist, newmtx = configCom.getSkew(1)
        skewObject.setSkewMtx(mtx, dist, newmtx)
        # Process board image
        image1 = skew_correction(image1, skewObject)

        # Grabs scale info from config
        dictionary = configCom.getScale()

        scale_detect = ScaleDetection()
        scale_detect.setScale(dictionary['x_scale'], dictionary['y_scale'], dictionary['units'])


        #finalImage = stitch_images(image1, image2)
        finalImage = image1
        cv2.imwrite('FinalImage.jpg', finalImage)
        contours, contourImage = find_contours(np.array(finalImage, dtype=np.uint8))
        xscale, yscale, units = get_scale(scale_detect)
        export_json(contours, xscale, yscale, units) #do I need to do something with return value?


        return contourImage #do we want to show the contours on this as well?

    def doesConfigExist(self):
        """
        Checks to see if we have run calibration yet
        Args:
            None
        Returns:
            True if we have config file, False if we don't
        """
        if (scale_calibration_data()):
            return True
        else:
            return False
