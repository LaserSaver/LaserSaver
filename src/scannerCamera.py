import cv2
import numpy as np
import logging

class ScannerCamera:
    '''
    Class for determining and storing intrinsic camera values
    '''
    
    def __init__(self):
        
        # Which camera am I?
        self.camera_number = None
        
        # Camera scaling metrics
        self.x_scale = None
        self.y_scale = None
        
        # Skew correction matrices
        self.skew_dst = None
        self.skew_roi = None
     
    ''' TAKE PHOTOS '''    
    def takePhoto(self):
        
        return 0
        
        
    ''' SKEW CORRECTION ''' 
    def calibrateSkewCorrection(self):
        
        return 0
       
    def findSkewCorrectionValues(self, calibImages):
        
        return 0
        
        
    ''' FINDING SCALE '''
    def calibrateScale(self):
        
        return 0
        
        
        
        
        
        
        
        
        
        