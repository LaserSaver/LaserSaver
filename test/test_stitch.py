import unittest
from stitch import Stitcher

imageA = cv2.imread("test/left1.jpg")
imageB = cv2.imread(args["test/right1.jpg"])

def testNoImagesFail():
    pass

def testSimpleImages():
    imageA = imutils.resize(imageA, width=400, height=400)
    imageB = imutils.resize(imageB, width=400, height=400)

    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    assert result != None
