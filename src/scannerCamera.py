import cv2
import numpy as np
import logging
from determineSkew import DetermineSkew


class ScannerCamera:
    '''
    Class for determining and storing intrinsic camera values
    '''
    
    
    def __init__(self, camera_number):
        ''' Initializes ScannerCamera 
                - needs camera_number, which will be assigned by user
            
            Args:
                camera_number (int): Which camera this object refers to
        '''
        
        # Which camera am I?
        self.camera_number = camera_number
        
        # Skew correction matrices
        self.skew_dst = None
        self.skew_roi = None
        
        # Are we using skew correction?
        self.use_skew_correction = None
        
     
    ''' Pull values from config file '''
    def setFromConfig(self):
        
        return 0   
    
   
    ''' Calibrate Skew Correction '''
    
    def setSkewCorrectionValues(self, calib_photos):
        ''' Finds dst and roi for a list of calibration photos
            - sets class variables
            
        Args:
            calib_photos: list of photos taken specifically for skew calibration
            
        Returns:
            None
        
        '''
        
        # If self.use_skew_correction = None, then we are calibrating for skew
        self.use_skew_correction = None
        
        # Find dst and roi matrices
        dst, roi, _ = DetermineSkew.createSkewMatrix(calib_photos)
        
        self.skew_dst = dst
        self.skew_roi = roi
        
    
    def setUseSkewCorrection(self, save_skew_correction):
        ''' Based on user feedback, determines if we will save the dst and roi values
        
        Args:
            save_skew_correction (bool): If True, we will be applying skew correction to images, if False we will not be using skew correction
        
        Returns:
            None
        '''
        
        self.use_skew_correction = save_skew_correction
        
    
        
    ''' TAKE PHOTOS '''    
    def takePhoto(self):
        
        return 0
    
        
    ''' Correct image skew '''
    
    def correctSkew(self, original_img):
        '''
        Applies skew matrix values to a given photo
            - Only applys dst if use_skew_correction = True or None
                - None implies this is being used for calibration purposes
                - If user has turned skew correction off, then it just returns the original image
        
        Args:
            original_img (string): photo which needs skew correction
            
        Returns:
            If using skew correction:
                corrected_img (string): photo corrected for skew
            Else:
                original_img (string): the unaltered original image
        '''
        
        if self.use_skew_correction is None:
            
            # This means that the image we are using for calibration is permanently rewritten with the skew matrix
            corrected_img = cv2.imwrite(original_img, self.skew_dst)
            return corrected_img
            
        elif self.use_skew_correction is True:
            
            corrected_img = cv2.imwrite(original_img, self.skew_dst)
            return corrected_img

        else:
            return original_img
            

        


        