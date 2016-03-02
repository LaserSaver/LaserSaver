import findContours
import scaleDetection
import stitch
import gui

scaleDetect = ScaleDetection()

def calibration(image, objx, objy):
    scaleDetect.calibrate(image, objx, objy)

def gui_start_screen():
    a = 0

def gui_calibration_screen():
    a = 0

def gui_take_pictures_screen():
    a = 0

def gui_enter_thickness_screen():
    a = 0

#Is this function needed?
def gui_export_screen():
    a = 0

def main():
    gui_start_screen()

    #Calibration
    calibration()




if __name__ == "__main__":
    main()