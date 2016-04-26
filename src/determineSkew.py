import numpy as np
import cv2
from copy import deepcopy
import logging

class DetermineSkew:
    ''' 
    Skew Correction
    '''
    
    ''' CLASS METHODS '''
    shape = (4, 11)
    
    @staticmethod
    def createSkewMatrix(calibImages):
        '''
        Finds matrix needed to deskew photo based on a list of images
            - also finds approximate error of matrix
        
        Args:
            calibImages: list of circleGrid photos taken for calibration
            
        Returns:
            dst: matrix which will correct skew when applied to an image
            roi:
            error: calculated error value for skew matrix
        '''
        
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
        
        if calibImages == []:
            logging.debug("No images to calibrate from")
            raise AttributeError
        
        objpoints, imgpoints = DetermineSkew.findSkewPoints(calibImages)
        
        if imgpoints == [] or objpoints == []:
            logging.debug("Could not find pattern centers, cannot continue with calibration")
            raise AttributeError
        
        h, w = calibImages[0].shape[:2]
        
        _, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, (w,h), None, None)
        
        logging.debug("New image time...")
    
        img = calibImages[0]
        
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

        logging.debug("ROI is: ")
        logging.debug(roi)

        
        return mtx, dist, newcameramtx


        # logging.debug("Undistorting...")
        #
        # # UNDISTORT ------
        # dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
        #
        #
        # logging.debug("Done undistorting...")
        #
        # logging.debug("DST is: ")
        # logging.debug(dst)
        #
        #
        # logging.debug("Writing new image")
        #
        #
        # cv2.imwrite('calibresult.png',dst)
        #
        # error = DetermineSkew.correctionAccuracy(objpoints, imgpoints, rvecs, tvecs, mtx, dist)
        # print error
        #
        # return dst, roi, error

    @staticmethod   
    def findSkewPoints(calibImages):
        '''
        Takes in a series of images of a 11x4 circleGrid pattern, 
        locates their major center points,
        and places them in two matrices
    
        Args: 
            calibImages: list of circleGrid photos taken for calibration
    
        Returns:
            objpoints: 3D points in real world space
            imgpoints: 2D points in image plane

        '''
    
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
        
        
        if calibImages == []:
            raise AttributeError
        
    
        # Initialize arrays
        centers = np.zeros((6*7), np.float32)
    
        pattern_points = np.zeros( (np.prod(DetermineSkew.shape), 3), np.float32)
        pattern_points[:,:2] = np.indices(DetermineSkew.shape).T.reshape(-1, 2)

    
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane


        x = 0

    
        logging.debug("Starting loop")
        for fname in calibImages[1:]:
            logging.debug("In loop")
            logging.debug(x)
            img = fname
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Image must be greyscale for center finding to work.
            
            # h, w = gray.shape[:2]
    
            logging.debug("Got images")

        
            # Find circle centers
            [ret, centers] = cv2.findCirclesGrid(gray, DetermineSkew.shape, centers, cv2.CALIB_CB_ASYMMETRIC_GRID + cv2.CALIB_CB_CLUSTERING)
    
    
            logging.debug("Done finding centers")
            logging.debug(" ")
        
            if ret == True:
        
                criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
                logging.debug("Found centers")

                centers2 = cv2.cornerSubPix(gray, centers, DetermineSkew.shape, (-1,-1), criteria)
            
                imgpoints.append(deepcopy(centers2.reshape(-1,2)))
                objpoints.append(pattern_points)

                # Draw and display the corners
                logging.debug("Drawing corners")
            
                img = cv2.drawChessboardCorners(img, DetermineSkew.shape, centers, ret)
                # cv2.imshow('img', img)
#                 cv2.waitKey(0)
#
                x = x+1
            
            else:
                logging.debug("No corners here, bub.")
                logging.debug(ret)
                logging.debug(centers)
                # cv2.imshow('img', img)
#                 cv2.waitKey(0)
            
                x = x+1

        # cv2.destroyAllWindows()
        
        
        return objpoints, imgpoints
        
        
    
    @staticmethod
    def correctionAccuracy(objpoints, imgpoints, rvecs, tvecs, mtx, dist):
        ''' Calculates error of skew correction
            - Should be as close to 0 as possible
        '''
    
        tot_error = 0
        for j in xrange(len(objpoints)):
            imgpoints2, _ = cv2.projectPoints(objpoints[j], rvecs[j], tvecs[j], mtx, dist)
            imgpoints2 = imgpoints2.reshape(-1,2)
            error = cv2.norm(imgpoints[j], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
            tot_error += error
    
        return tot_error/len(objpoints)    
