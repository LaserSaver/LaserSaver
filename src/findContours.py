import cv2
import numpy as np
import logging


'''
NOTES:
        - Will display grayscale version of original image, as well as a contour-only image
            - Press any key to dismiss image windows (when image windows are in focus)
        - Takes a few extra seconds to print out contour coordinates
'''
class FindContours:
    '''
        Does useful stuff with contours
    '''
    def __init__(self):
        return

    @staticmethod
    def find_all_contours(img):
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
            img (string): Original image of board

        Returns:
            initial_contours: list of all contours in image
            hierarchy: initial_contours hierarchy
            edgeImage: the edge image the contours were built off


        '''

        #img = cv2.imread(img,0)

        # Edge detection
        edgeImage = cv2.Canny(img,200,400)

        # Use copy of edges1 if we want to preserve orignal edges, as cv2.threshold() is destructive
        edgeCopy = edgeImage.copy()

        # Finding contours
        ret,thresh = cv2.threshold(edgeCopy,127,255,0)

        # cv2.findContours returns an image (which we don't need), the list of identified contours,
        # and the contour hierarchy(how the contours relate to each other)
        _, initial_contours, hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

        return initial_contours, hierarchy, edgeImage

    @staticmethod
    def select_contours(contours, hierarchy):
        '''Selects the relevant contours from set of all contours found in an image

        - Loops through every contour found in an initial image
            - identifies where each contour sits in the overall hierarchy
                - if contour has no parent, this is a contour we want to return
                    => add it to finalContours

        Args:
            contours: list of all contours of an image
            hierarchy: contours hierarchy

        Returns:
            finalContours: list of every contour of interest

        '''


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

        #LOGGING
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')

        # List of selected contours
        finalContours = []


        i=0 #Total contours found
        j=0 #Final contours selected
        for cnt in contours:

            # If contour has no parent... Then it's one we want
            if hierarchy[0][i][3] == -1:

                logging.debug("--------------")
                logging.debug("NEW CONTOUR " + str(i))
                logging.debug(hierarchy[0][i][3])

                '''
                Positive contour areas = features, Negative areas = holes
                Or, at least, they should be if there weren't double contours --> all areas we find are currently negative
                Contour w/ largest absolute value should be the edge of the entire board
                '''
                logging.debug("Contour area: " + str(cv2.contourArea(cnt,True)) )

                logging.debug("END CONTOUR " + str(i))
                logging.debug("--------------")

                # Add good contour to list
                finalContours.append(cnt)

                j += 1

            i += 1


        logging.debug(str(i) + " Total Contours Found")
        logging.debug(str(j) + " Final Contours Found")

        return finalContours

    @staticmethod
    def display_drawn_contours(inputImg, contourList):
        '''Draws given contours on a new image, and displays the image to the user

        Args:
            inputImg (string): the original photo
            contourList: list of contours found in photo

        Returns:
            drawnContours: image of the given contours
        '''
        
        # print inputImg.shape

        drawing = np.zeros(inputImg.shape,np.uint8)
        drawnContours = cv2.drawContours(drawing, contourList, -1, (255,255,255), 1)

        # THIS IS A HACK!!!!
        # For some reason we are unable to display the drawCountours in the 
        #  GUI so the two lines below are a hack!
        cv2.imwrite("contours.jpg", drawnContours)

        img = cv2.imread("contours.jpg", 0)

        return img
