import json

class jsonCreator:
    '''
    A class to construct a json object for exportation
    '''
    def __init__(self, logger = None):
        '''
        Initialize a new jsonCreator object.  This will call the resetJson function to set all values to None.
        Keyword Arguments:
            logger (logger object): Logger object to debug this class, will be set to None if no object is specified.
        '''
        if logger is not None:
            self.logger = logger
        self.resetJson()
    def addScale(self, x, y):
        '''
        This function will add the scale to the json object
        Keyword Arguments:
            x (float): The scale of the x axis
            y (float): The scale of the y axis
        '''
        try:
            if type(x) is not float:
                raise TypeError
            if type(y) is not float:
                raise TypeError
        except TypeError:
            if self.logger is not None:
                self.logger.debug("X and Y must be floats")
            return -1
        self.__json["scale"] = (x,y)
        return 0
    def addContours(self, contour):
        '''
        This function will add the scale to the json object
        Keyword Arguments:
            contour (list): the contour(s) to be added this can be a list of vertices or a list of contours (list of lists)
        '''
        try:
            if type(contour) is not list:
                raise TypeError
        except TypeError:
            if self.logger is not None:
                self.logger.debug("Contour must be of type list")
            return -1
        if type(contour[0]) is list:
            self.__json["contours"] += contour
        else:
            self.__json["contours"].append(contour)
        return 0
    def getJson(self):
        '''
        Returns: A dict containing the added information.
        '''
        return self.__json
    def exportJson(self):
        '''
        This function is a placeholder for when it will eventually be exported over the internet.
        Returns: A json object that has been dumped into a string for exporting
        '''
        return json.dumps(self.__json)
    def resetJson(self):
        '''
        Resets the JSON object to empty all variables
        '''
        self.__json = {}
        self.__json["scale"] = None
        self.__json["contours"] = []
