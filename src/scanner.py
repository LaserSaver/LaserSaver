import findContours
import scaleDetection
import stitch
import gui
import determineSkew
import scannerCamera
import jsoncreator

#detSkew = DetermineSkew()

def scale_calibration(image, objx, objy):
    success = scaleDetect.calibrate(image, objx, objy)
    scaleDetect.saveConfigFile()
    return success

def scale_calibration_data():
    success = scaleDetect.loadConfigFile()
    #load other calibration data as well
    return success

def get_scale(thickness):
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
    jsonData.addUnits(units)
    jsonData.addContours(contours)
    jsonData.addScale(xscale, yscale)
    return jsonData.exportJson()

class Scanner:

    #Functions GUI should call:
    def first(self):
        scaleDetect = ScaleDetection()
        jsonData = jsonCreator()
        #load calibration data
        scaleDataExists = scale_calibration_data()

        #if calibration data doesn't exist, ask user to calibrate
        if (not scaleDataExists):
            image, objx, objy = gui_scale_calibration_screen()
            scale_calibration(image, objx, objy)


    def second(self, calibImages1, calibImages2):


    def main():


        #ask user if they want to calibrate if skew calibration data doesn't exist
        calibImages1, calibImages2 = gui_skew_calibration_screen()
        dst1, roi1 = skew_calibration(calibImages1)
        dst2, roi2 = skew_calibration(calibImages2)

        image1, image2 = gui_take_pictures_screen()

        cam1Settings = ScannerCamera()
        cam2Settings = ScannerCamera()

        image1 = skew_correction(image1, dst1, roi1, cam1Settings)
        image2 = skew_correction(image2, dst2, roi2, cam2Settings)

        finalImage = stitch_images(image1, image2)
        contours, edgeImage = find_contours(finalImage)

        #what should happen if they don't like the image? Do we go back to start?
        thickness = gui_enter_thickness_screen(edgeImage)

        #would scale just be multiplied by (height - thickness)/height?
        xscale, yscale = get_scale(thickness)

        units = gui_export_screen()

        export_json(contours, xscale, yscale, units) #do I need to do something with return value?



if __name__ == "__main__":
    main()