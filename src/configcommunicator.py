import configparser
import json


class configcommunicator():
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
        Args: True if calibration has been completed
        '''
        if type(value) is not dict:
            raise TypeError
        self.config.set("Scale Calibration", "scale", json.dumps(value))

    def getScale(self):
        return json.loads(self.config.get("Scale Calibration", "scale"))

    def setSkipSkew(self, value):
        if type(value) is not bool:
            raise TypeError
        self.config.set("Skew Calibration", "skip_skew", str(value))

    def getSkipSkew(self):
        return bool(self.config.get("Skew Calibration", "skip_skew"))

    def setSkew(self, value, camera_num):
        self.config.set("Skew Calibration", "camera" + str(camera_num), json.dumps({'skew':value}))
        self.config.set("Skew Calibration", "skip_skew", str(False))

    def getSkew(self, camera_num):
        return json.loads(self.config.get("Skew Calibration", "camera" + str(camera_num))).get('skew')

    def saveConfig(self):
        with open(self.filename, 'wb') as fp:
            self.config.write(fp)

if __name__ == "__main__":
    cc = configcommunicator()
    print cc.checkValidity()
    #print cc.getSkipSkew()
    #print cc.getSkipSkew()
    #cc.setScale({'x':5,'y':4})
    #cc.setSkew([[50, 3, 4],[5,2,4]], 1)
    #cc.setSkew([[500, 30, 40],[50,20,40]], 2)
    print cc.getSkipSkew()
    print cc.getSkew(1)
    print cc.getSkew(2)
    cc.saveConfig()
