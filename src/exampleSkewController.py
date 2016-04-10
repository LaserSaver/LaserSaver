import cv2
import numpy as np
from scannerCamera import ScannerCamera

class ExampleSkewController():
    ''' Example of a how the Skew Calibration will function '''
    
    @staticmethod
    def takeCalibrationPhotos():
        ''' User will take a set of photos of calibration image
        '''
        
        image_2 = cv2.imread('images/image_2.jpeg',0)
    
        cv2.imwrite('images/skew_test_1.jpeg', image_2)
        
        testImgs = ['images/skew_test_1.jpeg','images/image_2.jpeg','images/image_3.jpeg', 'images/image2_7.jpeg','images/image3_10.jpeg', 'images/image3_30.jpeg', 'images/image4_1.jpeg', 'images/image5_1.jpeg', 'images/image6_1.jpeg','images/image7_1.jpeg','images/image8_1.jpeg','images/image9_1.jpeg','images/image10_1.jpeg','images/image11_1.jpeg','images/image12_1.jpeg','images/image13_1.jpeg','images/image14_1.jpeg','images/image15_1.jpeg','images/image16_1.jpeg','images/image17_1.jpeg','images/image18_1.jpeg','images/image19_1.jpeg','images/image20_1.jpeg','images/image21_1.jpeg']
        
        return testImgs
        
                
    ''' GET USER FEEDBACK '''
    @staticmethod
    def getCalibFeedback(img):
        ''' Feedback from user about whether or not the image looks okay
                - Interaction w/ GUI
        '''
        
        return False
    
    @staticmethod    
    def continueSkewCalib():
        ''' Feedback from user about whether or not to abandon skew correction for now
                - Interaction w/ GUI
        '''
        
        return False
        

    
    ''' SKEW CORRECTION CALIBRATION IN ITS ENTIRETY ---> ESSENTIALLY WHAT THE CONTROLLER CODE SHOULD LOOK LIKE '''
    @staticmethod
    def calibrateSkewCorrection():
        '''
        Calibrates the skew values for a given scanner camera
        
            - Takes series of calibration photos
                - GUI interaction
            
            - Calls createSkewMatrix on a list of calibration photos
                - gets dst and roi
                - sets self.dst == dst
                - sets self.roi == roi
            
            
            - Selects a test_img from list of calibration photos
                - or has user take a specific photo for this use
                    - first image taken is the test photo 
                        --> displayed corrected to user, but won't be used in calibration
            
            - Applys dst/roi to test_img
            
            - Displays test_img to user
                - asks user if test_img looks okay
                    
            - if calibration not okay: 
                - won't permanently save dst and roi
                - asks user if they would like to re-calibrate, or proceed without skew correction
            
                - if re-calibrate: 
                    - return false
            
                - if proceed w/o calibration:
                    - sets self.dst == None
                    - sets self.roi == None
                    - return true
                    
            - if calibration okay:
                - return true
                
        Args:
            None
        Returns:
            True: when done with calibration

        '''
        # Initializes ScannerCamera object
        ourCamera = ScannerCamera(0)
        
        print "Hello, we will now start Skew Calibration"
        
        # Loop until finished
        while True:
        
            print "Starting loop..."
            
            # User takes calibration photos
            calib_photos = ExampleSkewController.takeCalibrationPhotos()
        
            # Find dst, roi
            ourCamera.setSkewCorrectionValues(calib_photos)
        
            # Correct skew on a test image
            test_img = calib_photos[0]
            test_img = ourCamera.correctSkew(test_img)
        
            # User tells us if calibration looks okay based on test_img
            skew_okay = ExampleSkewController.getCalibFeedback(test_img)
            
            # Set whether or not we will continue to use skew correction on future images
            ourCamera.setUseSkewCorrection(skew_okay)
        
            # Finishing skew calibration
            
            if skew_okay is True:
                # If the image looked correct, we'll break the loop
                print "Break Loop 1"
                break
            
            else:
                # Check if we want to keep trying to calibrate skew
                retry_skew = ExampleSkewController.continueSkewCalib()
                
                if retry_skew is True:
                    print "Continue Loop"
                    continue
                else:
                    print "Break Loop 2"
                    break
        
        return True
        
def main():
    test = ExampleSkewController.calibrateSkewCorrection()
    
    print test
    
    
    
if __name__ == '__main__':
    main()