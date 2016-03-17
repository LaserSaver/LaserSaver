import cv2
import logging
from determineSkew import DetermineSkew

def main():

    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    
    image_2 = cv2.imread('images/image_2.jpeg',0)
    
    cv2.imwrite('images/skew_test_1.jpeg', image_2)
    
    testImgs = ['images/skew_test_1.jpeg','images/image_2.jpeg','images/image_3.jpeg', 'images/image2_7.jpeg','images/image3_10.jpeg', 'images/image3_30.jpeg', 'images/image4_1.jpeg', 'images/image5_1.jpeg', 'images/image6_1.jpeg','images/image7_1.jpeg','images/image8_1.jpeg','images/image9_1.jpeg','images/image10_1.jpeg','images/image11_1.jpeg','images/image12_1.jpeg','images/image13_1.jpeg','images/image14_1.jpeg','images/image15_1.jpeg','images/image16_1.jpeg','images/image17_1.jpeg','images/image18_1.jpeg','images/image19_1.jpeg','images/image20_1.jpeg','images/image21_1.jpeg']


    _, _, error = DetermineSkew.createSkewMatrix(testImgs)
    
    print "Done"
    print "Calculated error = " + str(error)
    
    img1 = cv2.imread('smallRealBoard1.JPG')
    img2 = cv2.imread('calibresult.png')
    # cv2.imshow("ORIGINAL", img1)
    # cv2.imshow("CORRECTED", img2)
    # cv2.waitKey(0)
    
    
if __name__ == "__main__":
    main()