import cv2
import numpy as np
import logging
import determineSkew

class ScannerCamera:
    '''
    Class for determining and storing intrinsic camera values
    '''
    
    
    def __init__(self):

        # Camera scaling metrics
        self.x_scale = None
        self.y_scale = None
        
        # Skew correction matrices
        self.skew_dst = None
        self.skew_roi = None
        
        # Using skew correction?
        # If camera calibration is too far off, it would definitely 
        # be better to just not use the skew correction at all
        # If saved in config file, can also be used to determine
        # whether first time calibrating
        self.use_skew_correction = None
     
    ''' TAKE PHOTOS '''    
    def takePhoto(self):
        
        return 0
        
    def takeCalibrationPhotos(self):
        
        testImgs = ['smallRealBoard1.JPG','images/image_2.jpeg','images/image_3.jpeg', 'images/image2_7.jpeg','images/image3_10.jpeg', 'images/image3_30.jpeg', 'images/image4_1.jpeg', 'images/image5_1.jpeg', 'images/image6_1.jpeg','images/image7_1.jpeg','images/image8_1.jpeg','images/image9_1.jpeg','images/image10_1.jpeg','images/image11_1.jpeg','images/image12_1.jpeg','images/image13_1.jpeg','images/image14_1.jpeg','images/image15_1.jpeg','images/image16_1.jpeg','images/image17_1.jpeg','images/image18_1.jpeg','images/image19_1.jpeg','images/image20_1.jpeg','images/image21_1.jpeg']
        
        return testImgs
        
        
    ''' GET USER FEEDBACK '''
    
    def getCalibFeedback(self, img):
        
        return True
        
    def continueSkewCalib(self):
        
        return True
        
        
    ''' SKEW CORRECTION ''' 
    
    def calibrateSkewCorrection(self):
        '''
        Calibrates the skew values for a given scanner camera
        
            - Takes series of calibration photos
                - GUI interaction
            
            - Calls createSkewMatrix on a list of calibration photos
                - gets dst and roi
                - sets self.dst == dst
                - sets self.roi == roi
                
            - check error (returned from createSkewMatrix())
                
                - if error > [threshold]:
                    - tell user calibration is bad
                    - ask if they would like to re-calibrate or proceed w/o skew correction
                        
                        - if re-calibrate: 
                            - return false
            
                        - if proceed w/o calibration:
                            - sets self.dst == None
                            - sets self.roi == None
                            - return true
                
                - if error <= [threshold]:
                    - continue
            
            - Selects a test_img from list of calibration photos
                - or has user take a specific photo for this use
                    - first image taken is the test photo 
                        --> displayed corrected to user, but won't be used in calibration
            
            - Applys dst/roi to test_img
            
            - Displays test_img to user
                - asks user if test_img looks okay
                    
            - if calibration not okay: 
                - doesn't save dst and roi
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
            True: if calibration is finished, whether values have been saved or not
            False: if calibration needs to be restarted

        '''
        
        calib_photos = takeCalibrationPhotos()
        
        dst, roi, error = DetermineSkew.createSkewMatrix(testImgs)
        
        self.skew_dst = dst
        self.skew_roi = roi
        
        feedback = getCalibFeedback(testImgs[0])
        
        if feedback is False:
            self.skew_dst = None
            self.skew_roi = None
            
            continue_calibration = continueSkewCalib()
            
            if continue_calibration is True:
                return False
            
            else:
                self.use_skew_correction = False
        
        else:
            self.use_skew_correction = True
        
        return True
        
        
    def correctSkew(self, original_img):
        '''
        Applies skew matrix values to a given photo
            - Only applys dst if use_skew_correction = True
                - If user has turned skew correction off, then it just returns the original image
        
        Args:
            original_img (string): photo which needs skew correction
            
        Returns:
            corrected_img (string): photo corrected for skew
        '''
        if self.use_skew_correction is True:

            corrected_img = cv2.imwrite(original_img, self.skew_dst)
            return corrected_img

        else:
            return original_img
 
        
        
        
    ''' FINDING SCALE '''
    def calibrateScale(self):
        
        return 0
        
        
        
        
        
        
        
        
        
        