#####
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
from playsound import playsound

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtGui import QFont, QFontDatabase
import time
import random

################################################################################################
# Convert UI to PyQt5 py file
################################################################################################
os.system("pyuic5 -o interface_ui.py interface.ui")

################################################################################################
# Import UI file
################################################################################################

from interface_ui import *




################################################################################################
# MAIN WINDOW CLASS
################################################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        ################################################################################################
        # Setup the UI main window
        ################################################################################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ################################################################################################
        # Show window
        ################################################################################################c
        
        self.show()
        
        #check
        ################################################################################################
        # CUSTOMIZE ANALOGUE GAUGE WIDGET
        ################################################################################################
        self.ui.widget.enableBarGraph =True

        ################################################################################################
        # Set gauge units
        ################################################################################################
        self.ui.widget.units = " Km/h"

        ################################################################################################
        # Set minimum gauge value
        ################################################################################################
        self.ui.widget.minValue =0

        ################################################################################################
        # Set maximum gauge value
        ################################################################################################
        self.ui.widget.maxValue =250

        ################################################################################################
        # Set scale divisions
        ################################################################################################
        self.ui.widget.scalaCount = 10
        #check
        # Start from the minimum value
        # self.ui.widget.minValue=3

        # OR
        # Start from half/middle value
        # self.ui.widget.updateValue(int(self.ui.widget.maxValue - self.ui.widget.minValue)/2)
        # self.ui.widget.updateValue(self.ui.widget.maxValue)
        
        
        #self.ui.widget.updateValue(10)
        
        
        

        ################################################################################################
        # Select gauge theme
        ################################################################################################
        # 0 to 24
        # check
        #self.ui.widget.setGaugeTheme(20)
        # check

        #self.ui.widget.setCustomGaugeTheme(
        #     color1 = "#FF00A6", #bright
        #     color2= "#870058", #middle brightness
        #     color3 = "#360023" #darkest
        # )
        # check
        #women _desgin
        #self.ui.widget.setCustomGaugeTheme(
        #     color1 = "#360023", #darkest
        #     color2= "#870058", #middle brightness
        #     color3 = "#FF00A6" #bright
        # )
        # check
        # self.ui.widget.setCustomGaugeTheme(
        #     color1 = "#00F6E9",
        #     color2= "#990008",
        #     color3 = "#002523"
        # )
        # check
        #self.ui.widget.setCustomGaugeTheme(
        #     color1 = "#fff", #white
        #     color2= "#555", #grey
        #     color3 = "#000" #black
        # )
        # check
        self.ui.widget.setCustomGaugeTheme(
             color1 = "#000", #black
             color2= "#555", #grey
             color3 = "#fff" #white
        )
        # check
        # self.ui.widget.setCustomGaugeTheme(
        #     color1 = "orange",
        #     color2 = "blue"
        # )
        # check
        self.ui.widget.setScalePolygonColor(
             color1 = "white",
             color2 = "white",
             color3 = "white"
        )
        # check
        #self.ui.widget.setNeedleCenterColor(
           #  color1 = "white",
            # color2 = "orange",
            # color3 = "green"
        #)
        # check
        self.ui.widget.setScaleValueColor(255,255,250,255)
        # self.ui.widget.setOuterCircleColor(
        #     color1 = "#22FF00",
        #     color2 = "#000",
        #     color3 = "#021200"
        # )
        #self.ui.widget.setNeedleCenterColor(
         #    color1 = "white",
         #    color2 = "red",
          #   color3 = "white"
        #)
        # check
        self.ui.widget.setBigScaleColor("red")
        # check
        self.ui.widget.setFineScaleColor("black")

        ################################################################################################
        # Set custom font
        ################################################################################################
        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), 'fonts/ds_digital/DS-DIGIB.TTF') )
        # check
        #self.ui.widget.setValueFontFamily("DS-Digital")
        #self.ui.widget.setScaleFontFamily("DS-Digital")
        # check
        self.ui.widget.setNeedleColor(255, 255,150, 255)
        # check
        self.ui.widget.setNeedleColorOnDrag(255, 255, 0, 255)
        # check
        # self.ui.widget.setScaleValueColor(34, 255, 0, 255)
        # check
        self.ui.widget.setDisplayValueColor(255,250,255,255)
        # check
        #self.ui.widget.setEnableBarGraph(False)
        # check
        #self.ui.widget.setEnableValueText(True)
        # check
        self.ui.widget.setEnableCenterPoint(False)
        # check
        #self.ui.widget.setEnableNeedlePolygon(False)
        # check
        # self.ui.widget.setEnableScaleText(False)
        # check
        #self.ui.widget.setEnableScalePolygon(False)
        # check
        # self.ui.widget.setEnableBigScaleGrid(False)
        # check
        # self.ui.widget.setEnableFineScaleGrid(False)
        self.ui.widget.setMouseTracking(False)

       
     
        


########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

########################################################################
## END===>
########################################################################  
