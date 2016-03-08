import cv2
import numpy as np
from findContours import FindContours

def main():
    
    input_img = 'images/whiteBackTest2.png'
    
    # List of contours, and image of edges
    
    exampleContours = FindContours()
    
    initialContourList, listHierarchy, drawnEdges = exampleContours.find_all_contours(input_img)
    
    finalContourList = exampleContours.select_contours(initialContourList, listHierarchy)
    
    input_img = cv2.imread('images/smallRealBoard1.jpg', 0)
    
    finalImage = exampleContours.display_drawn_contours(input_img,finalContourList)
    
    return finalContourList
    
    
    
    
    
if __name__ == '__main__':
    main()