from nose.tools import *
import cv2
import imutils
from stitch import Stitcher

IMAGEA = cv2.imread("left1.jpg")
IMAGEB = cv2.imread("right1.jpg")
IMAGEC = cv2.imread("left2.jpg")


def testStichPass():
    imageA = imutils.resize(IMAGEA, width=400, height=400)
    imageB = imutils.resize(IMAGEB, width=400, height=400)

    # stitch the images together to create a panorama
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    # show the images (commented out for using pi through ssh)
    cv2.imshow("Result", result)
    assert result != None


@raises(TypeError)
def testStichFail():
    imageA = imutils.resize(IMAGEC, width=400, height=400)
    imageB = imutils.resize(IMAGEB, width=400, height=400)

    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

def testDetectAndDescribePass():
    imageA = imutils.resize(IMAGEA, width=400, height=400)
    stitcher = Stitcher()
    (kpsA, featuresA) = stitcher.detectAndDescribe(imageA)
    assert kpsA != None and featuresA != None


def testDetectAndDescirbeFail():
    pass

def testmatchKeyPointsPass():
    pass

def testmatchKeyPointsFail():
    pass

def testdrawMatchesPass():
    pass

def testdrawMatchesFail():
    pass
