import cv2
import numpy as np
from findContours import FindContours

def main():
    
    input_img = 'images/smallWhiteBackTest3.jpg'
    
    # List of contours, and image of edges
    initialContourList, listHierarchy, drawnEdges = FindContours.find_all_contours(input_img)
    
    finalContourList = FindContours.select_contours(initialContourList, listHierarchy)
    
    input_img = cv2.imread('images/smallRealBoard1.jpg', 0)
    
    finalImage = FindContours.display_drawn_contours(input_img,finalContourList)
    
    return finalContourList
    
    
    
    
    
if __name__ == '__main__':
    main()