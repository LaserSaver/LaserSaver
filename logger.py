import logging

'''
To Use logger in your own file

from logger import logger

newlogger = logger(loglevel = 'debug', cmdline = True).getLogger()
newlogger.debug("Debug Message")
newlogger.info('Info Message')
'''

class logger():
    def __init__(self, loggerName = 'LaserCutter', loglevel = "info", cmdline = False, filename = "lasercutter.log"):
    '''
    Initialize a new logger
    :param loggerName: Name of Logger default is Lasercutter
    :type loggerName: String
    :param loglevel: Level of Log set to 'debug' for debug mode.  Default is 'info'
    :type loglevel: String
    :param cmdline: Paramaeter to log to cmdline. Default is False
    :type cmdline: Boolean
    :param filename: Name of logging file.  Default is 'lasercutter.log'
    :type filename: String
    '''
        if loglevel == "debug":
            level = logging.DEBUG
        else:
            level = logging.INFO
        formatter = logging.Formatter('%(name)s: %(levelname)s - %(message)s')
        self.logger = logging.getLogger(loggerName)
        if(cmdline):
            cmd_handler = logging.StreamHandler()
            cmd_handler.setLevel(level)
            cmd_handler.setFormatter(formatter)
            self.logger.addHandler(cmd_handler)
        file_handler = logging.FileHandler(filename = filename, mode = 'a', encoding = None, delay = False)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level)

    #returns an instance of the logger
    def getLogger(self):
        '''
        Returns the initialized logger
        :rtype: logger instance
        '''
        return self.logger
