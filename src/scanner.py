import findContours
import scaleDetection
import stitch
import determineSkew
import scannerCamera
import jsoncreator

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
    success = scaleDetect.calibrate(image, objx, objy, units)
    scaleDetect.saveConfigFile()
    return success

def scale_calibration_data():
    """
    See if scale calibration data exists
    Args:
        None
    Returns:
        True on success, False on failure
    """
    success = scaleDetect.loadConfigFile()
    #load other calibration data as well
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

def skew_calibration(calibImages):
    """
    desc
    Args:
        None
    Returns:
        True on success, False on failure
    """
    dst, roi, error = DetermineSkew.createSkewMatrix(calibImages)
    return dst, roi

def skew_correction(image, dst, roi, camSettings):
    """
    desc
    Args:
        None
    Returns:
        True on success, False on failure
    """
    return camSettings.correctSkew(image)

def stitch_images(image1, image2):
    """
    desc
    Args:
        None
    Returns:
        True on success, False on failure
    """
    return Stitcher.stitch((image1,image2)) #correct order for images?

def find_contours(image):
    """
    desc
    Args:
        None
    Returns:
        True on success, False on failure
    """
    #findContours = FindContours()
    contours, hierarchy, edgeImage = FindContours.find_all_contours(image)
    finalContours = findContours.select_contours(contours, hierarchy)
    return finalContours,edgeImage

def export_json(contours, xscale, yscale, units):
    """
    desc
    Args:
        None
    Returns:
        True on success, False on failure
    """
    jsonData = jsonCreator()
    jsonData.addUnits(units)
    jsonData.addContours(contours)
    jsonData.addScale(xscale, yscale)
    return jsonData.exportJson()

class Scanner:
    #in case we want to pass around 1 scanner object instead of the individual objects
    def __init__(self):
        '''
        Initialize a new Scanner object
        '''
        cam1Settings = None
        cam2Settings = None
        scaleDetectObj = None

    #Functions GUI should call:
    def scaleCalibration(self, image1, image2, objx, objy, units):
        """
        Calibrates scale detection object and returns it
        Args:
            image1: image from camera 1 for scale detection
            image2: image from camera 2 for scale detection
            objx: width of calibration object
            objy: height of calibration object
            units (string): units to use
        Returns:
            scaleDetect: ScaleDetection object needed later
        """
        image = stitch_images(image1, image2)
        scaleDetect = ScaleDetection()
        scale_calibration(scaleDetect, image, objx, objy, units)
        return scaleDetect #returned in order to be passed to detect_contours


    def skewCalibration(self, calibImages):
        """
        Skew calibration. Should be run on each camera
        Args:
            calibImages: calibration images for camera 1 (any number)
        Returns:
            camSettings: ScannerCamera object
        """
        dst, roi = skew_calibration(calibImages)
        camSettings = ScannerCamera()
        camSettings.skew_dst = dst
        camSettings.skew_roi = roi
        return camSettings#returns this to be put in next function

    def processImages(self, image1, image2, cam1Settings, cam2Settings, scaleDetect):
        """
        The rest of the logic to stitch the image
        Args:
            image1: image from camera 1
            image2: image from camera 2
            cam1Settings: ScannerCamera object for camera 1
            cam2Settings: ScannerCamera object for camera 2
            scaleDetect: scale detection object previously used
        Returns:
            finalImage: image to be displayed to user to confirm it is correct
        """
        cam1Settings = ScannerCamera()
        cam2Settings = ScannerCamera()

        image1 = skew_correction(image1, cam1Settings)
        image2 = skew_correction(image2, cam2Settings)

        finalImage = stitch_images(image1, image2)
        contours, edgeImage = find_contours(finalImage)
        xscale, yscale = get_scale(scaleDetect)
        units = scaleDetect.units
        export_json(contours, xscale, yscale, units) #do I need to do something with return value?
        return finalImage #do we want to show the contours on this as well?

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