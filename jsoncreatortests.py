from jsoncreator import jsonCreator
from logger import logger
import unittest

class TestJsonCreator(unittest.TestCase):
    '''
    Tests basic functionality of the jsonCreator object
    '''
    def setUp(self):
        '''
        Sets up the testing environment
        '''
        self.log = logger(loglevel = "info", cmdline = True).getLogger()
        self.jc = jsonCreator(logger = self.log)
        self.jc.addScale(2.,3.)
        self.jc.addContours([(5,3),(4,6)])
        self.jc.addContours([[(2,3)], [(2,6),(4,8)]])
    def testContours(self):
        '''
        Verifies that the contours are set correctly
        '''
        output = self.jc.getJson()
        self.assertItemsEqual(output.get("contours"), [[{"x":5,"y":3},{"x":4,"y":6}], [{"x":2,"y":3}], [{"x":2,"y":6},{"x":4,"y":8}]])
    def testScale(self):
        '''
        Verifies that the scale is set correctly.
        '''
        output = self.jc.getJson()
        self.assertEqual(output.get("scale"),(2,3))
    def testContourTypeCheck(self):
        '''
        Verifies the type checking is working correctly for the Contours
        '''
        self.assertRaises(TypeError, self.jc.addContours(4))
    def testScaleTypeCheck(self):
        '''
        Verifies the type checking is working correctly for the scale.
        '''
        self.assertRaises(TypeError, self.jc.addScale(4, 2.))
    def testReset(self):
        '''
        Verifies that the resetJson object is workign correclty
        '''
        self.jc.resetJson()
        output = self.jc.getJson()
        self.assertEqual(output.get("scale"), None)
        self.assertEqual(output.get("contours"), [])

if __name__ == '__main__':
    unittest.main()
