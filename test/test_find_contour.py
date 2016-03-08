import unittest
from nose.tools import assert_raises
from findContours import FindContours

''' Contour Finding (by number of cnts returned)'''
def test_no_image():
    # test = FindContours()
    # assert_raises(AttributeError, test.find_all_contours("", False))
    pass

def test_simple_image():
    test = FindContours()
    cnts, hierarchy, _ = test.find_all_contours('test/simpleLaser.jpg', False, False)
    finalCnts = FindContours.select_contours(cnts, hierarchy)
    assert len(finalCnts) == 7
    
def test_small_real_image():
    test = FindContours()
    cnts, hierarchy, _ = test.find_all_contours('test/smallRealBoard1.jpg', False, False)
    finalCnts = FindContours.select_contours(cnts, hierarchy)
    assert len(finalCnts) == 11
    
def test_large_real_image():
    pass

def test_complicated_image():
    pass

''' EDGE THRESHOLD ALTERATION '''

def test_default_max_threshold():
    test = FindContours()
    assert test.edge_max_thresh == 400
    
def test_default_min_threshold():
    test = FindContours()
    assert test.edge_min_thresh == 200

def test_decrease_threshold():
    test = FindContours()
    test.decreaseEdgeThresh()
    assert (test.edge_max_thresh == 350) and (test.edge_min_thresh == 150)
    
def test_increase_threshold():
    test = FindContours()
    test.increaseEdgeThresh()
    assert (test.edge_max_thresh == 450) and (test.edge_min_thresh == 250)
    
