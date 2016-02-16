import unittest
from nose.tools import assert_raises
from findContours import FindContours

def test_no_image():
    assert_raises(AttributeError, FindContours.find_all_contours, "")

def test_simple_image():
    cnts, hierarchy, _ = FindContours.find_all_contours('simpleLaser.jpg')
    finalCnts = FindContours.select_contours(cnts, hierarchy)
    assert len(finalCnts) == 7
    
def test_small_real_image():
    cnts, hierarchy, _ = FindContours.find_all_contours('smallRealBoard1.jpg')
    finalCnts = FindContours.select_contours(cnts, hierarchy)
    assert len(finalCnts) == 11
    
def test_large_real_image():
    pass
    
def test_complicated_image():
    pass
    