from scaleDetection import ScaleDetection
from decimal import *
import json


def testCalibration():
    image = 'test.jpg'
    sd = ScaleDetection()
    sd.calibrate(image, 30.2, 30.2)
    w,h = (3012.616455078125, 2951.0859375)
    assert round(sd.x_scale * Decimal(w), 1) == 30.2
    assert round(sd.y_scale * Decimal(h), 1) == 30.2


def testScale():
    image = 'test.jpg'
    sd = ScaleDetection()
    sd.x_scale = 0.01002450874524511436479390460
    sd.y_scale = 0.01023352102907033668498759679
    w,h = sd.detectSize(image)
    assert round(w, 1) == 30.2
    assert round(h, 1) == 30.2


def testSaveConfig():
    image = 'test.jpg'
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
    image = 'test.jpg'
    cf = 'test.conf'
    sd = ScaleDetection()
    sd.loadConfigFile(config_file=cf)
    assert sd.x_scale is not None
    assert sd.y_scale is not None
