import unittest
import cv2
import imutils
from stitch import Stitcher

IMAGEA = cv2.imread("test/left1.jpg")
IMAGEB = cv2.imread("test/right1.jpg")

def testNoImagesFail():
    pass

def testSimpleImages():
    imageA = imutils.resize(IMAGEA, width=400, height=400)
    imageB = imutils.resize(IMAGEB, width=400, height=400)

    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    assert result != None
