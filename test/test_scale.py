from scaleDetection import ScaleDetection
from decimal import *
import json


# all [x, y]
SAVE_IMG = False
TEST_CONF = 'test/test.conf'

FILENAME = 'test/tester1.jpg'
IMG_DIM = [5, 5]
IMG_PIX = (359.0, 359.0)
SCALE = [0.01392757660167130919220055710, 0.01392757660167130919220055710]

FILENAMES = ['test/tester1.jpg', 'test/tester2.jpg',
          'test/tester3.jpg', 'test/tester4.jpg',
          "test/tester5.jpg", 'test/tester9.jpg']
# [x, y]
DIMS = [[5, 5], [3.0, 8.0], [4.0, 4.0], [8.0, 4.0], [14.222, 10.667], [10, 7]]
UNIT = "in"

def testDimensions():
    sd = ScaleDetection()
    im = sd.openImage(FILENAME)
    w, h = sd.getDimensions(im)
    assert w == IMG_PIX[0]
    assert h == IMG_PIX[1]

def testCalibration():
    sd = ScaleDetection()
    im = sd.openImage(FILENAME)
    sd.calibrate(im, IMG_DIM[0], IMG_DIM[1], UNIT)
    w,h = IMG_PIX
    assert round(sd.x_scale * Decimal(w), 0) == IMG_DIM[0]
    assert round(sd.y_scale * Decimal(h), 0) == IMG_DIM[1]


def testCalibrationFail():
    sd = ScaleDetection()
    im = sd.openImage(FILENAME)
    f = sd.calibrate(im, IMG_DIM[0], "a", UNIT)
    assert f == False


def testCalibrationFailIm():
    sd = ScaleDetection()
    f = sd.calibrate("a", IMG_DIM[0], IMG_DIM[1], UNIT)
    assert f == False


def testScales():
    for i in range(0, len(FILENAMES)):
        sd = ScaleDetection()
        sd.x_scale = SCALE[0]
        sd.y_scale = SCALE[1]
        sd.units = UNIT
        im = sd.openImage(FILENAMES[i])
        w,h,unit = sd.getSize(im, show_conts=SAVE_IMG)
        print "Width: {}".format(round(w,1))
        print "Height: {}".format(round(h,1))
        assert round(w, 1) == round(DIMS[i][0], 1)
        assert round(h, 1) == round(DIMS[i][1], 1)


def testSaveConfig():
    cf = TEST_CONF
    sd = ScaleDetection()
    sd.x_scale = SCALE[0]
    sd.y_scale = SCALE[1]
    sd.units = UNIT
    sd.saveConfigFile(config_file=cf)
    with open(cf, 'r') as conf:
        j = json.load(conf)
    assert j["x_scale"] == sd.x_scale
    assert j["y_scale"] == sd.y_scale
    assert j["units"] == UNIT


def testLoadConfig():
    cf = TEST_CONF
    sd = ScaleDetection()
    sd.loadConfigFile(config_file=cf)
    assert sd.x_scale is not None
    assert sd.y_scale is not None
    assert sd.units is not None


def testLoadConfigFail():
    cf = "abc"
    sd = ScaleDetection()
    f = sd.loadConfigFile(config_file=cf)
    assert f == False


def testChain():
    sd = ScaleDetection()
    im = sd.openImage(FILENAME)
    sd.calibrate(im, IMG_DIM[0], IMG_DIM[1], UNIT)
    im = sd.openImage(FILENAMES[-1])
    w, h, unit = sd.getSize(im, show_conts=SAVE_IMG)
    print "Width: {}".format(round(w,1))
    print "Height: {}".format(round(h,1))
    assert round(w, 1) == round(DIMS[-1][0], 1)
    assert round(h, 1) == round(DIMS[-1][1], 1)
