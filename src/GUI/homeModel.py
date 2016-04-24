import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scanner import Scanner

class HomeModel:
    def __init__(self):
        self.scanner = Scanner()
        
    def doesScaleExist(self):
        """
        Calls the scanner doesConfigExist 
        Returns:
            True on success, False on failure
        """
        return self.scanner.doesConfigExist()
        