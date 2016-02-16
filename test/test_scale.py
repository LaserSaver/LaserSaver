#from scanner import ScaleDetection
from scaleDetection import ScaleDetection
from decimal import *
import json


# all [x, y]
SAVE_IMG = True
TEST_CONF = 'test/test.conf'

IMAGE = 'test/tester1.jpg'
IMG_DIM = [5, 5]
IMG_PIX = (359.0, 359.0)
SCALE = [0.01392757660167130919220055710, 0.01392757660167130919220055710]

IMAGES = ['test/tester1.jpg', 'test/tester2.jpg',
          'test/tester3.jpg', 'test/tester4.jpg',
          "test/tester5.jpg", 'test/tester9.jpg']
# [x, y]
DIMS = [[5, 5], [3.0, 8.0], [4.0, 4.0], [8.0, 4.0], [14.222, 10.667], [10, 7]]

# IMAGE = 'test/power_brick.jpg'
# IMG_DIM = [139.2, 64.5]
# IMG_PIX = (1494.58288574, 3298.8046875)
# SCALE = [0.09313635351235495464600164007, 0.01955253678534128128796652196]

# IMAGE_2 = 'test/canon.jpg'
# IMG_DIM_2 = [87.5, 69]

def testDimensions():
    sd = ScaleDetection()
    w, h = sd.getDimensions(IMAGE)
    assert w == IMG_PIX[0]
    assert h == IMG_PIX[1]

def testCalibration():
    sd = ScaleDetection()
    sd.calibrate(IMAGE, IMG_DIM[0], IMG_DIM[1])
    w,h = IMG_PIX
    assert round(sd.x_scale * Decimal(w), 0) == IMG_DIM[0]
    assert round(sd.y_scale * Decimal(h), 0) == IMG_DIM[1]


def testCalibrationFail():
    sd = ScaleDetection()
    f = sd.calibrate(IMAGE, IMG_DIM[0], "a")
    assert f == False


def testCalibrationFailIm():
    sd = ScaleDetection()
    f = sd.calibrate("a", IMG_DIM[0], IMG_DIM[1])
    assert f == False


def testScales():
    for i in range(0, len(IMAGES)):
        sd = ScaleDetection()
        sd.x_scale = SCALE[0]
        sd.y_scale = SCALE[1]
        w,h = sd.getSize(IMAGES[i], show_conts=SAVE_IMG)
        print round(w,1)
        print round(h,1)
        assert round(w, 1) == round(DIMS[i][0], 1)
        assert round(h, 1) == round(DIMS[i][1], 1)


def testSaveConfig():
    cf = TEST_CONF
    sd = ScaleDetection()
    sd.x_scale = SCALE[0]
    sd.y_scale = SCALE[1]
    sd.saveConfigFile(config_file=cf)
    with open(cf, 'r') as conf:
        j = json.load(conf)
    assert j["x_scale"] == sd.x_scale
    assert j["y_scale"] == sd.y_scale


def testLoadConfig():
    cf = TEST_CONF
    sd = ScaleDetection()
    sd.loadConfigFile(config_file=cf)
    assert sd.x_scale is not None
    assert sd.y_scale is not None


def testLoadConfigFail():
    cf = "abc"
    sd = ScaleDetection()
    f = sd.loadConfigFile(config_file=cf)
    assert f == False


def testChain():
    sd = ScaleDetection()
    sd.calibrate(IMAGE, IMG_DIM[0], IMG_DIM[1])
    w, h = sd.getSize(IMAGES[-1], show_conts=SAVE_IMG)
    print round(w,0)
    print round(h,0)
    assert round(w, 1) == round(DIMS[-1][0], 1)
    assert round(h, 1) == round(DIMS[-1][1], 1)
