import cv2
import numpy as np
from contourDetection import ContourDetection

class ExampleFindImageContours():
    
    @staticmethod
    def findImageContours(input_img):
    
        # List of contours, and image of edges
    
        exampleContours = ContourDetection()
        
        initial_contour_list, list_hierarchy, drawn_edges = exampleContours.findAllContours(input_img, True)
        
        final_contour_list = exampleContours.selectContours(initial_contour_list, list_hierarchy)
        
        input_img = cv2.imread('images/smallRealBoard1.jpg', 0)
        
        finalImage = exampleContours.displayDrawnContours(input_img,final_contour_list)
        
        return final_contour_list
    

def main():
    
    # input_img = 'images/whiteBackTest2.png'
    input_img = 'images/smallRealBoard1.jpg'
    
    final_contour_list = ExampleFindImageContours.findImageContours(input_img)
    
    return final_contour_list
    
    
    
    
    
if __name__ == '__main__':
    main()