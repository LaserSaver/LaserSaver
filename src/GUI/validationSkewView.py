from appUtils import *
from baseView import BaseView

class ValidationSkewView(BaseView):
    def __init__(self, master, controller, img):
        ''' Sets up the skew validation contours view screen
        Args:
        master(Tk object): The toplevel widget of Tk which is the main window of an application
        controller(ValidationSkewController object): The controller which will be in charge of the view
        img(Image): The resulting image from the skew model processing
        '''
        BaseView.__init__(self, master)
        self.addTitle("Does this look okay?")
        
    def configImgPanel(img, imgPanel):
        cv2.imwrite('IMPORTANTTEST.jpg', img)
        resizedImg = AppUtils.converImgToTkinterImg(img, master.winfo_width()-50, master.winfo_height()-165)
        imgPanel.configure(width=master.winfo_width()-50, height=master.winfo_height()-165, relief=RIDGE, borderwidth=2, image = resizedImg)
        imgPanel.image = resizedImg
        
        self.imgPanel = Label(self)
        configImgPanel(img, self.imgPanel)
        self.imgPanel.bind("<Configure>", lambda e: configImgPanel(img, self.imgPanel) )
        self.imgPanel.pack(side=TOP)
        
        self.redoButton = Button(self, text="No, return to calibrating skew", command=controller.redoClicked)
        self.redoButton.pack(side=BOTTOM)
        continueText = "Yes, continue to scale calibration"
        self.continuteButton = Button(self, text=continueText, command=controller.continueClicked)
        self.continuteButton.pack(side=BOTTOM)


