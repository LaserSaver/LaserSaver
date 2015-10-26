import cv2
# import json
import numpy as np


'''
NOTES:
        - Will display grayscale version of original image, as well as a contour-only image
            - Press any key to dismiss image windows (when image windows are in focus)
        - Takes a few extra seconds to print out contour coordinates
'''

def find_edges(img):
    '''
    Returns image of detected edges from original image
        Currently both original and copy 
    
    Utilizes Canny algorithm for edge detection
    
    Threshold numbers are compared to calculated Gradient values
    Max: Anything above definitely an edge
    Min: Anything below definitely NOT an edge
    
    '''

    # Actual edge detection
    # Current threshold numbers are fairly arbitrary, although they are fairly accurate
    # We will likely want to alter these as they
    edges1 = cv2.Canny(img,200,400)
    
    
    # Use copy of edges1, or original gets destroyed
    copy = edges1.copy()

    return edges1, copy

  
def find_contours(img):
    '''
    Finds contours of image, and draws them
        Returns: list of found contours, image of drawn contours, and the edge image it was built off
    
    Each individual contour is a numpy array of (x,y) coordinates of boundary points of the object.
    
    '''
    
    # Get modified image
    # edgeImage is the original edge image, modImg is the copy
    edgeImage, modImg = find_edges(img)

    
    # Where we will draw the contours, I guess???
    drawing = np.zeros(img.shape,np.uint8) 
    
    
    # Finding contours
    # Want to use modImg, as this is destructive
    ret,thresh = cv2.threshold(modImg,127,255,0)

    # CHAIN_APPROX_NONE will store ALL contour boundary pts --> More memory usage, but more accurate
    # We don't really need the returned image at this point
    # RETR_CCOMP assumes a 2-level hierarchy
    _, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    
    

    '''
    EXTRACTING CORRECT CONTOURS --- (ASSUMING THERE ARE CONTOURS OTHER THAN THOSE OF THE BOARD)

        - FIND CONTOUR W/ LARGEST AREA --> THIS SHOULD BE THE SHEET ITSELF
        - REMOVE CONTOURS WHOSE X AND Y VALUES ARE NOT WITHIN THOSE OF THE LARGEST CONTOUR
        - ALL REMAINING CONTOURS SHOULD REPRESENT FEATURES OF THE BOARD
    '''
 
    
    '''
    LOOP THROUGH ALL CONTOURS AND ONLY DRAW ONE SET OF CORRECT CONTOURS
       
        - THERE ARE MULTIPLE DIFFERENT CONTOURS AROUND EACH EDGE
            - ONLY WANT THE ONE SET
    
    '''
    i=0
    j=0
    for cnt in contours:

        # If contour has no parent... Then it's one we want
        if hierarchy[0][i][3] == -1:
        
            print "--------------"
            print "NEW CONTOUR " + str(i)
            print hierarchy[0][i][3]
            
            # Positive areas = features, Negative areas = holes
            # Or, at least, they should be if there weren't double contours --> all areas we find are currently negative
            # Contour w/ largest absolute value should be the edge of the entire board
            print cv2.contourArea(cnt,True)
            
            for pnt in cnt:
                print pnt
        
            print "END CONTOUR " + str(i)
            print "--------------"

            # There might be a contour surrounding the entire image, and we don't want that
            # if cnt[0][0][0] == 1 and cnt[0][0][1] == 1:
            #     print "THIS ONE IS SURROUNDING THE ENTIRE IMAGE"
            #     cntToRem = i
                #break
                

            cv2.drawContours(drawing, contours, i, (255,255,255), 1)
            j += 1
            
        i += 1
        
    print str(i) + " Total Contours Found"
    print str(j) + " Final Contours Found"
    
    
    
    return contours, drawing, edgeImage
    
    


def main():
    
    # If exporting to contour data to file,
    #   first clear the file of previous text
    
    # open('contourOutput.txt', 'w').close()
    
    print "STARTING NOW"
    
    '''
     Select input image
        - Will eventually grab image directly from camera
    '''
    # Complicated image
    # inputImg = cv2.imread('laser1.jpg',0)
    
    # Simple image
    # inputImg = cv2.imread('simpleLaser.jpg',0)
    
    # Real image (small)
    inputImg = cv2.imread('smallRealBoard1.jpg',0)
    
    # Real image (big)
    # inputImg = cv2.imread('realBoard1.jpg',0)
    
    
    '''
    Find contours
    '''
    
    # List of contours, and two images
    contourList, drawnContours, drawnEdges = find_contours(inputImg)
    
    # Display various process images
    
    '''
    Display images
    '''
    
    cv2.imshow("Start", inputImg)
    # cv2.imshow("Edges", drawnEdges)
    cv2.imshow("Contours", drawnContours)


    # Any key press closes all display windows (while windows are in focus)
    cv2.waitKey(0)
    

    
if __name__ == "__main__":
    main()
    
