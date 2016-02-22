import cv2
import logging
from calibrateSkew import CalibrateSkew

def main():

    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    
    testImgs = ['images/image_2.jpeg','images/image_3.jpeg', 'images/image2_7.jpeg','images/image3_10.jpeg', 'images/image3_30.jpeg', 'images/image4_1.jpeg', 'images/image5_1.jpeg', 'images/image6_1.jpeg','images/image7_1.jpeg','images/image8_1.jpeg','images/image9_1.jpeg','images/image10_1.jpeg','images/image11_1.jpeg','images/image12_1.jpeg','images/image13_1.jpeg','images/image14_1.jpeg','images/image15_1.jpeg','images/image16_1.jpeg','images/image17_1.jpeg','images/image18_1.jpeg','images/image19_1.jpeg','images/image20_1.jpeg','images/image21_1.jpeg']


    _, _, error = CalibrateSkew.createSkewMatrix(testImgs)
    
    print "Done"
    print "Calculated error = " + str(error)
    
    
    
if __name__ == "__main__":
    main()