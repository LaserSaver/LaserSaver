import configparser


class configcommunicator():
    def __init__(self, filename = 'LaserCutterConfig.conf'):
        '''
        Initialize a new logger that logs
        Keyword Arguments:
            filename (str): Name of logging file.  Default is 'lasercutter.log'
        '''
        self.filename = filename
        try:
            self.config = configparser.ConfigParser()
            self.config.read(filename)
            if self.config.items.length() <= 2:
                raise BaseException
        except:
            print "caught"
            open(self.filename, 'w').close()
            self.config.add_section('Skew Calibration')
            self.config.add_section('Scale Calibration')
        print config.items()

    def CheckValidity(self):
        if self.config.has_option("Scale Calibration", "scale")  && self.config.has_optin("Skew Calibration", "skip_skew")

    def setScale(self, value):
        if type(value) is not dict:
            raise TypeError
        self.config.set("Scale Calibration", "scale", value)

    def getScale(self, value):
        return self.config.get("Scale Calibration", "scale")

    def setSkipSkew(self, value):
        if type(value) is not bool:
            raise TypeError
        self.config.set("Skew Calibration", "skip_skew", value)

    def getSkipSkew(self, camera_num):
        return self.config.get("Skew Calibration", "skip_skew")

    def setSkew(self, value, camera_num):
        if type(value) is not dict:
            raise TypeError
        self.config.set("Skew Calibration", "camera" + str(camera_num), value)
        self.config.set("Skew Calibration", "skip_skew", False)

    def getSkew(self, camera_num):
        return self.config.get("Skew Calibration", "camera" + str(camera_num))

    def saveConfig(self):
        self.config.write(self.filename)

if __name__ == "__main__":
    cc = configcommunicator()
