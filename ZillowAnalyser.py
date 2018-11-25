from PySide.QtGui import QApplication, QMainWindow, QIcon, QHBoxLayout, \
    QWidget, QSplitter
from PySide.QtCore import Qt, QSettings
import sys, os



class ZillowAnalyserWindow(QMainWindow):
    def __init__(self):
        super(ZillowAnalyserWindow,self).__init__()
        self.setWindowTitle("Zillow Analyser")

        #todo add window
        #self.setWindowIcon()
        self.settings=QSettings("StNono Soft","Zillow Analyser")

        if self.settings.value("geometry"):
            self.restoreGeometry(self.settings.value("geometry"))