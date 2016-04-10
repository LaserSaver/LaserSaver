import unittest
from nose.tools import assert_raises
from determineSkew import DetermineSkew

''' TEST DetermineSkew.findSkewPoints() '''

def test_findSkewPoints_0_images():
    assert_raises(AttributeError, DetermineSkew.findSkewPoints, [])
    
def test_findSkewPoints_1_image():
    pass
    
def test_findSkewPoints_10_images():
    pass
    
def test_findSkewPoints_20_images():
    pass


''' TEST DetermineSkew.createSkewMatrix() '''

def test_createSkewMatrix_0_images():
    assert_raises(AttributeError, DetermineSkew.createSkewMatrix, [])
    
def test_createSkewMatrix_1_image():
    pass
    
def test_createSkewMatrix_10_images():
    pass
    
def test_createSkewMatrix_20_images():
    pass
    
    
    
''' TEST SKEW CORRECTION ACCURACY '''
def test_more_images_mean_less_error_10_vs_1():
    pass
    
def test_more_images_mean_less_error_20_vs_10():
    pass

    
    
    
