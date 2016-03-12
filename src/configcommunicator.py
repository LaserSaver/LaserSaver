import configparser


class configcommunicator():
    def __init__(self, filename = 'thisfile.conf'):
        '''
        Initialize a new logger that logs
        Keyword Arguments:
            filename (str): Name of logging file.  Default is 'lasercutter.log'
        '''
        try:
            config = configparser.ConfigParser()
            config.read(filename)
        except:
            print "caught"
            open(filename, 'w').close()
            config.add_section('Skew Calibration')
            config.add_section('Scale Calibration')
            return
        print config.items()

    def calibrateScale(self):
        return

if __name__ == "__main__":
    cc = configcommunicator()
