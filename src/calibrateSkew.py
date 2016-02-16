import numpy as np
import cv2
import glob
from copy import deepcopy



def findCenters(calibImages):
    
    
    # Shape of calibration pattern
    shape = (4, 11)
    
    
    # Initialize arrays
    centers = np.zeros((6*7), np.float32)
    
    pattern_points = np.zeros( (np.prod(shape), 3), np.float32)
    pattern_points[:,:2] = np.indices(shape).T.reshape(-1, 2)

    
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane
    
    

    x = 0

    
    print "Starting loop"
    for fname in calibImages:
        print "In loop"
        print x
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Image must be greyscale for center finding to work.
    
        print "Got images"
        
        h, w = gray.shape[:2]
        print h
        print w
        
        # Find circle centers
        [ret, centers] = cv2.findCirclesGrid(gray, shape, centers, cv2.CALIB_CB_ASYMMETRIC_GRID + cv2.CALIB_CB_CLUSTERING)
    
    
        print "Done finding centers"
        print " "
        
        if ret == True:
        
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
            print "Found centers"

            centers2 = cv2.cornerSubPix(gray, centers, shape, (-1,-1), criteria)
            
            imgpoints.append(deepcopy(centers2.reshape(-1,2)))
            objpoints.append(pattern_points)
            
            # print imgpoints
            # print objpoints

            # Draw and display the corners
            print "Drawing corners"
            
            img = cv2.drawChessboardCorners(img, shape, centers, ret)
            cv2.imshow('img', img)
            cv2.waitKey(0)
            
            x = x+1
            
        else:
            print "No corners here, bub."
            print ret
            print centers
            cv2.imshow('img', img)
            cv2.waitKey(0)
            
            x = x+1

    cv2.destroyAllWindows()
    
    
    ret2, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, (w,h), None, None)
    
    
    print "New image time..."
    
    img = cv2.imread('smallRealBoard1.jpg')
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

    print "ROI is: "
    print roi


    print "Undistort time!"


    # REMAPPING ------
    # mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
    # dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)


    # UNDISTORT ------
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)


    print "Done undistorting..."

    print "DST is: "
    print dst


    print "Writing new image"
    cv2.imwrite('calibresult.png',dst)
    
    error = correctionAccuracy(objpoints, imgpoints, rvecs, tvecs, mtx, dist)
    # print error
    
    mean_error = error/len(objpoints)
    print mean_error
    
    
def correctionAccuracy(objpoints, imgpoints, rvecs, tvecs, mtx, dist):
    
    tot_error = 0
    for j in xrange(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[j], rvecs[j], tvecs[j], mtx, dist)
        imgpoints2 = imgpoints2.reshape(-1,2)
        error = cv2.norm(imgpoints[j], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
        tot_error += error
    
    return tot_error/len(objpoints)    



def main():
    
    testImgs = ['image_2.jpeg','image_3.jpeg', 'image2_7.jpeg','image3_10.jpeg', 'image3_30.jpeg', 'image4_1.jpeg', 'image5_1.jpeg', 'image6_1.jpeg','image7_1.jpeg','image8_1.jpeg','image9_1.jpeg','image10_1.jpeg','image11_1.jpeg','image12_1.jpeg','image13_1.jpeg','image14_1.jpeg','image15_1.jpeg','image16_1.jpeg','image17_1.jpeg','image18_1.jpeg','image19_1.jpeg','image20_1.jpeg','image21_1.jpeg']

    findCenters(testImgs)
    
    print "Done"
    
    
    
if __name__ == "__main__":
    main()