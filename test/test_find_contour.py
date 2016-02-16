import unittest

from findContours import find_contours

def test_no_image():
    # find_contours("")
    # assert_raises(AttributeError)
    pass

def test_simple_image():
    _, numContours, _ = find_contours('test/simpleLaser.jpg')
    assert numContours == 7

def test_small_real_image():
    _, numContours, _ = find_contours('test/smallRealBoard1.jpg')
    assert numContours == 11

def test_large_real_image():
    pass

def test_complicated_image():
    pass
