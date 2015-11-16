from scanner import ScaleDetection
from decimal import *
import json


IMAGE = 'tests/test.jpg'


def testCalibration():
    sd = ScaleDetection()
    sd.calibrate(IMAGE, 30.2, 30.2)
    w,h = (3012.616455078125, 2951.0859375)
    assert round(sd.x_scale * Decimal(w), 1) == 30.2
    assert round(sd.y_scale * Decimal(h), 1) == 30.2


def testCalibrationFail():
    sd = ScaleDetection()
    f = sd.calibrate(IMAGE, 30.2, "a")
    assert f == False


def testCalibrationFailIm():
    sd = ScaleDetection()
    f = sd.calibrate("a", 30.2, 30.2)
    assert f == False

def testScale():
    sd = ScaleDetection()
    sd.x_scale = 0.01002450874524511436479390460
    sd.y_scale = 0.01023352102907033668498759679
    w,h = sd.detectSize(IMAGE)
    assert round(w, 1) == 30.2
    assert round(h, 1) == 30.2


def testSaveConfig():
    cf = 'test.conf'
    sd = ScaleDetection()
    sd.x_scale = 0.01002450874524511436479390460
    sd.y_scale = 0.01023352102907033668498759679
    sd.saveConfigFile(config_file=cf)
    with open(cf, 'r') as conf:
        j = json.load(conf)
    assert j["x_scale"] == sd.x_scale
    assert j["y_scale"] == sd.y_scale


def testLoadConfig():
    cf = 'test.conf'
    sd = ScaleDetection()
    sd.loadConfigFile(config_file=cf)
    assert sd.x_scale is not None
    assert sd.y_scale is not None


def testLoadConfigFail():
    cf = "abc"
    sd = ScaleDetection()
    f = sd.loadConfigFile(config_file=cf)
    assert f == False
