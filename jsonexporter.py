import json
import requests

'''
Placeholder for after gabe reveals his server.
'''


class jsonExporter():
    '''
    A class to export the json object over http
    '''
    def __init__(self, URL, logger = None):
        '''
        Initialize a new jsonExporter object.  This will call the resetJson function to set all values to None.
        Args:
            URL (str): The URL to post the json message
            logger (logger object): Logger object to debug this class, will be set to None if no object is specified.
        '''
        if logger is not None:
            self.logger = logger
        self.url = URL
    def authorize():

    def post(self, json):
        
