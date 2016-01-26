import cv2
# import json
import numpy as np


'''
NOTES:
        - Will display grayscale version of original image, as well as a contour-only image
            - Press any key to dismiss image windows (when image windows are in focus)
        - Takes a few extra seconds to print out contour coordinates
'''
  
def find_contours(img):
    ''' Finds contours of given image
    
    - Utilizes Canny algorithm for edge detection
    
        - Threshold numbers are compared to calculated Gradient values
            Max: Anything above definitely an edge
            Min: Anything below definitely NOT an edge
            
            - Alter threshold numbers to change accuracy
    
    - Finds contours in image using cv2.findContours()
        - Assumes a 2-level hierarchy (cv2.RETR_CCOMP)
            - Every contour is the boundary between a hole and a feature
        - Each individual contour is a numpy array of (x,y) coordinates of boundary points of the object
            - cv2.CHAIN_APPROX_NONE stores every single point along contour
    
    Called from main()
        
    Args:
        img (jpg): Original image of board
    
    Returns: 
        finalContours: list of relevant contours
        edgeImage: the edge image the contour image was built off
    
    
    '''
    
    # Edge detection
    edgeImage = cv2.Canny(img,200,400)
    
    # Use copy of edges1 if we want to preserve orignal edges, as cv2.threshold() is destructive
    edgeCopy = edgeImage.copy()
    
    # Finding contours
    ret,thresh = cv2.threshold(edgeCopy,127,255,0)

    # cv2.findContours returns an image (which we don't need), the list of identified contours, 
    # and the contour hierarchy(how the contours relate to each other)
    _, initial_contours, hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    
    # Selects only useful contours, and places them into a list
    finalContours = select_contours(initial_contours, hierarchy)


    return finalContours, edgeImage
    
    
def select_contours(contours, hierarchy):
    '''
    EXTRACTING CORRECT CONTOURS --- (ASSUMING THERE ARE CONTOURS OTHER THAN THOSE OF THE BOARD)

        - FIND CONTOUR W/ LARGEST AREA --> THIS SHOULD BE THE SHEET ITSELF
        - REMOVE CONTOURS WHOSE X AND Y VALUES ARE NOT WITHIN THOSE OF THE LARGEST CONTOUR
        - ALL REMAINING CONTOURS SHOULD REPRESENT FEATURES OF THE BOARD
    '''
    
   # NOT CURRENTLY IMPLEMENTED, AS WE HAVE NO EXAMPLE IMAGE


    '''
    LOOP THROUGH ALL CONTOURS AND ONLY DRAW ONE SET OF CORRECT CONTOURS
   
        - THERE ARE MULTIPLE DIFFERENT CONTOURS AROUND EACH EDGE
            - ONLY WANT THE ONE SET

    '''
    # List of selected contours
    finalContours = []
    
    # Where we will draw the contours -> Sanity check, not needed for final product
    # drawing = np.zeros(img.shape,np.uint8)
    
    i=0 #Total contours found
    j=0 #Final contours selected
    for cnt in contours:
        
        # There might be a contour surrounding the entire image, and we don't want that
        # if cnt[0][0][0] == 1 and cnt[0][0][1] == 1:
        #     print "THIS ONE IS SURROUNDING THE ENTIRE IMAGE"
        #     cntToRem = i
        #     break

        # If contour has no parent... Then it's one we want
        if hierarchy[0][i][3] == -1:
    
            print "--------------"
            print "NEW CONTOUR " + str(i)
            print hierarchy[0][i][3]
        
            '''
            Positive contour areas = features, Negative areas = holes
            Or, at least, they should be if there weren't double contours --> all areas we find are currently negative
            Contour w/ largest absolute value should be the edge of the entire board
            '''
            print cv2.contourArea(cnt,True)
  
            # for pnt in cnt:
              # print pnt

            print "END CONTOUR " + str(i)
            print "--------------"
            
            # cv2.drawContours(drawing, contours, i, (255,255,255), 1)
            
            # Add good contour to list
            finalContours.append(cnt)
        
            j += 1
        
        i += 1
                

    print str(i) + " Total Contours Found"
    print str(j) + " Final Contours Found"
    
    print len(finalContours)
    
    return finalContours

def main():
    ''' Finds the contours from an image of the laser-cut board
    
    Currently only displays original image and created contour image
    Should eventually save these for later processing
    
    '''
    
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
    
    # List of contours, and image of edges
    contourList, drawnEdges = find_contours(inputImg)
        
    
    '''
    Display images
    '''
    drawing = np.zeros(inputImg.shape,np.uint8)
    
    drawnContours = cv2.drawContours(drawing, contourList, -1, (255,255,255), 1)
    
    cv2.imshow("Start", inputImg)
    # cv2.imshow("Edges", drawnEdges)
    cv2.imshow("Contours", drawnContours)


    # Any key press closes all display windows (while windows are in focus)
    cv2.waitKey(0)
    

    
if __name__ == "__main__":
    main()
    
