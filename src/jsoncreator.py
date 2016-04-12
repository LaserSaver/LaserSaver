import json

class jsonCreator:
    '''
    A class to construct a json object for exportation
    '''
    def __init__(self, logger = None):
        '''
        Initialize a new jsonCreator object.  This will call the resetJson function to set all values to None.
        Args:
            logger (logger object): Logger object to debug this class, will be set to None if no object is specified.
        '''

        self.logger = logger
        self.resetJson()

    def addUnits(self, units):
        '''
        This function will add the scale to the json object
        Args:
            x (float): The scale of the x axis
            y (float): The scale of the y axis
        '''
        if not isinstance(units, basestring):
            if self.logger is not None:
                self.logger.debug("Units must be a string")
            raise TypeError
        self.__json["units"] = units

    def addScale(self, x, y):
        '''
        This function will add the scale to the json object
        Args:
            x (float): The scale of the x axis
            y (float): The scale of the y axis
        '''
        '''
        try:
            if type(x) is not float:
                print type(x)
                raise TypeError
            if type(y) is not float:
                raise TypeError
        except TypeError:
            if self.logger is not None:
                self.logger.debug("X and Y must be floats")
            raise TypeError
        '''
        self.__json["scale"] = (str(x),str(y))

    def addContours(self, contours):
        '''
        This function will add the scale to the json object
        Args:
            contour (list): the contour(s) to be added this can be a list of vertices or a list of contours (list of lists)
        '''
        try:
            if type(contours) is not list:
                raise TypeError
        except TypeError:
            if self.logger is not None:
                self.logger.debug("Contour must be of type list")
            raise TypeError
        contours = contours[0]
        if type(contours[0]) is list:
            for contour in contours:
                contourdict = [{"x":c[0], "y":c[1]} for c in contour]
                self.__json["contours"].append(contourdict)
        else:
            for contour in contours:
                contourdict = [{"x":c[0], "y":c[1]} for c in contour]
                self.__json["contours"].append(contourdict)

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
        self.__json["units"] = None
        self.__json["contours"] = []
