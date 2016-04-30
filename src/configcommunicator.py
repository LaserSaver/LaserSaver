import configparser
import json
import numpy as np


class ConfigCommunicator():
    def __init__(self, filename = 'LaserCutterConfig.conf'):
        '''
        Initialize a config communicator object
        If a config file already exists load it's contents
        If not create a config file
        Args:
            filename (str): Name of config file.  Default is 'LaserCutterConfig.log'
        '''
        self.filename = filename
        try:
            self.config = configparser.ConfigParser()
            self.config.read(filename)
            sections = [section for section, item in self.config.items()]
            print sections
            if "Skew Calibration" not in sections or "Scale Calibration" not in sections:
                raise BaseException
        except:
            #print self.config.items()
            open(self.filename, 'w').close()
            self.config.add_section('Skew Calibration')
            self.config.add_section('Scale Calibration')

    def checkValidity(self):
        '''
        Check if calibration has been completed
        Returns:
            True if calibration has been completed, False if not
        '''
        if self.config.has_option("Scale Calibration", "scale")  and self.config.has_option("Skew Calibration", "skip_skew"):
            return True
        return False

    def setScale(self, value):
        '''
        Set the scale
        Args:
            value (dict): Scale calibration object
        '''
        if type(value) is not dict:
            raise TypeError
        self.config.set("Scale Calibration", "scale", json.dumps(value))

    def getScale(self):
        '''
        Retrieve scale calibration
        Returns:
            Scale Calibration (dict)
        '''
        try:
            json.loads(self.config.get("Scale Calibration", "scale"))
        except Exception:
            return None

        return json.loads(self.config.get("Scale Calibration", "scale"))

    def setSkipSkew(self, value):
        '''
        Set the skip_skew value
        Args:
            value (bool): Boolean indicating if skew calibration has been skipped
        '''
        if type(value) is not bool:
            raise TypeError
        self.config.set("Skew Calibration", "skip_skew", str(value))

    def getSkipSkew(self):
        '''
        Get the skip_skew value
        Returns:
            Boolean indicating if skew calibration has been skipped
        '''
        return bool(self.config.get("Skew Calibration", "skip_skew"))

    def setSkew(self, mtx_value, dist_value, newmtx_value,  camera_num):
        '''
        Set the skew calibration
        Args:
            value (list): Skew calibration dst
            camera_num (int): Camera which skew calibration corresponds too
        '''
        self.config.set("Skew Calibration", "camera" + str(camera_num), json.dumps({'mtx':mtx_value.tolist(), 'dist':dist_value.tolist(), 'newmtx':newmtx_value.tolist()}))
        self.config.set("Skew Calibration", "skip_skew", str(False))

    def getSkew(self, camera_num):
        '''
        Set the skew calibration
        Args:
            camera_num (int): Camera which skew calibration corresponds too
        Returns:
            Skew calibration (list) for camera_num
        '''

        mtx = np.array(json.loads(self.config.get("Skew Calibration", "camera" + str(camera_num))).get('mtx'))
        dist = np.array(json.loads(self.config.get("Skew Calibration", "camera" + str(camera_num))).get('dist'))
        newmtx = np.array(json.loads(self.config.get("Skew Calibration", "camera" + str(camera_num))).get('newmtx'))


        return mtx, dist, newmtx


    def saveConfig(self):
        '''
        Save the Config file to filename.
        '''
        with open(self.filename, 'wb') as fp:
            self.config.write(fp)
