import findContours
import scaleDetection
import stitch
import gui
import determineSkew
import scannerCamera
import jsoncreator

#detSkew = DetermineSkew()

def scale_calibration(image, objx, objy, units):
    success = scaleDetect.calibrate(image, objx, objy, units)
    scaleDetect.saveConfigFile()
    return success

def scale_calibration_data():
    success = scaleDetect.loadConfigFile()
    #load other calibration data as well
    return success

def get_scale(scaleDetect):
    return scaleDetect.getScale()

def skew_calibration(calibImages):
    dst, roi, error = DetermineSkew.createSkewMatrix(calibImages)
    return dst, roi

def skew_correction(image, dst, roi, camSettings):
    camSettings.skew_dst = dst
    camSettings.skew_roi = roi
    return camSettings.correctSkew(image)

def stitch_images(image1, image2):
    #stitcher = Stitcher()
    return Stitcher.stitch((image1,image2)) #correct order for images?

def find_contours(image):
    #findContours = FindContours()
    contours, hierarchy, edgeImage = FindContours.find_all_contours(image)
    finalContours = findContours.select_contours(contours, hierarchy)
    return finalContours,edgeImage

def export_json(contours, xscale, yscale, units):
    jsonData = jsonCreator()
    jsonData.addUnits(units)
    jsonData.addContours(contours)
    jsonData.addScale(xscale, yscale)
    return jsonData.exportJson()

def get_units():
    a = 0 #get from config

class Scanner:
    #Functions GUI should call:
    def scale_calibration(self, image, objx, objy, units):
        scaleDetect = ScaleDetection()
        scale_calibration(image, objx, objy, units)
        return scaleDetect #returned in order to be passed to detect_contours


    def skew_calibration(self, calibImages1, calibImages2):
        dst1, roi1 = skew_calibration(calibImages1)
        dst2, roi2 = skew_calibration(calibImages2)
        return dst1, roi1, dst2, roi2 #returns these to be put in next function

    def detect_contours(self, image1, image2, dst1, roi1, dst2, roi2, scaleDetect):
        cam1Settings = ScannerCamera()
        cam2Settings = ScannerCamera()

        image1 = skew_correction(image1, dst1, roi1, cam1Settings)
        image2 = skew_correction(image2, dst2, roi2, cam2Settings)

        finalImage = stitch_images(image1, image2)
        contours, edgeImage = find_contours(finalImage)
        xscale, yscale = get_scale(scaleDetect)
        units = get_units()
        export_json(contours, xscale, yscale, units) #do I need to do something with return value?

    def does_config_exist(self):
        if (scale_calibration_data()):
            return True
        else:
            return False