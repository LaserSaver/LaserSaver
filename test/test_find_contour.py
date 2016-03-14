import unittest
from nose.tools import assert_raises
from contourDetection import ContourDetection

''' Contour Finding (by number of cnts returned)'''
def test_no_image():
    # test = ContourDetection()
    # assert_raises(AttributeError, test.findAllContours("", False))
    pass

def test_simple_image():
    test = ContourDetection()
    cnts, hierarchy, _ = test.findAllContours('test/simpleLaser.jpg', False)
    final_cnts = test.selectContours(cnts, hierarchy)
    assert len(final_cnts) == 7
    
def test_small_real_image():
    test = ContourDetection()
    cnts, hierarchy, _ = test.findAllContours('test/smallRealBoard1.jpg', False)
    final_cnts = test.selectContours(cnts, hierarchy)
    assert len(final_cnts) == 11
    
def test_large_real_image():
    pass

def test_complicated_image():
    pass

''' EDGE THRESHOLD ALTERATION '''

def test_default_max_threshold():
    test = ContourDetection()
    assert test.edge_max_thresh == 400
    
def test_default_min_threshold():
    test = ContourDetection()
    assert test.edge_min_thresh == 200

def test_decrease_threshold():
    test = ContourDetection()
    test.decreaseEdgeThresh()
    assert (test.edge_max_thresh == 350) and (test.edge_min_thresh == 150)
    
def test_increase_threshold():
    test = ContourDetection()
    test.increaseEdgeThresh()
    assert (test.edge_max_thresh == 450) and (test.edge_min_thresh == 250)
    
