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
        Initialize a new logger that logs
        Keyword Arguments:
            loggerName (str): Name of Logger.  Default is 'Lasercutter'
            loglevel (str): Level of Log set to 'debug' for debug mode.  Default is 'info'
            cmdline (bool): Parameter to log to cmdline. Default is False
            filename (str): Name of logging file.  Default is 'lasercutter.log'
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

    def getLogger(self):
        '''
        Returns: The logger initialized when creating the class
        '''
        return self.logger
