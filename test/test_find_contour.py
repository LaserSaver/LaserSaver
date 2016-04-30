import unittest
import cv2
from nose.tools import assert_raises
from findContours import FindContours

def test_no_image():
    testimg = cv2.imread('',0)
    assert_raises(AttributeError, FindContours.find_all_contours, testimg)

def test_simple_image():
    testimg = cv2.imread('test/simpleLaser.jpg',0)
    cnts, hierarchy, _ = FindContours.find_all_contours(testimg)
    finalCnts = FindContours.select_contours(cnts, hierarchy)
    assert len(finalCnts) == 7
    
def test_small_real_image():
    testimg = cv2.imread('test/smallRealBoard1.jpg',0)
    cnts, hierarchy, _ = FindContours.find_all_contours(testimg)
    finalCnts = FindContours.select_contours(cnts, hierarchy)
    assert len(finalCnts) == 11
    
def test_large_real_image():
    pass

def test_complicated_image():
    pass
