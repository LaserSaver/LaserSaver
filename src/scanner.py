import findContours
import scaleDetection
import stitch
import gui

scaleDetect = ScaleDetection()
findContours = FindContours()

def scale_calibration(image, objx, objy):
    success = scaleDetect.calibrate(image, objx, objy)
    scaleDetect.saveConfigFile()
    return success

def calibration_data():
    success = scaleDetect.loadConfigFile()
    #load other calibration data as well
    return success

def skew_calibration(image):
    a = 0

def skew_correction(image):
    a = 0

def stitch_images(image1, image2):
    stitcher = Stitcher()
    return stitcher.stitch((image1,image2)) #correct order for images?

def find_contours(image):
    contours, hierarchy, edgeImage = findContours.find_all_contours(image)
    finalContours = findContours.select_contours(contours, hierarchy)
    return finalContours,edgeImage

def export_json(contours):
    a = 0

def gui_start_screen():
    a = 0

def gui_calibration_screen():
    a = 0

def gui_take_pictures_screen():
    a = 0

#Shows the board with contours
def gui_enter_thickness_screen(edgeImage):
    a = 0

#Is this function needed?
def gui_export_screen():
    a = 0

def main():
    gui_start_screen()

    #load calibration data
    calData = calibration_data()

    #if calibration data doesn't exist, ask user if they want to calibrate.
    if (not calData):
        calButton, image, objx, objy = gui_calibration_screen()
        if (calButton):
            scale_calibration(image, objx, objy)
            skew_calibration(image)#probably wrong place for this
            calData = calibration_data()

    image1, image2 = gui_take_pictures_screen()

    image1 = skew_correction(image1)
    image2 = skew_correction(image2)

    finalImage = stitch_images(image1, image2)
    contours, edgeImage = find_contours(finalImage)

    #what should happen if they don't like the image? Do we go back to start?
    thickness = gui_enter_thickness_screen(edgeImage)

    #scale calculation?

    export_json(contours)



if __name__ == "__main__":
    main()