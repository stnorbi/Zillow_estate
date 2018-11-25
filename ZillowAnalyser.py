from PySide.QtGui import QApplication, QMainWindow, QIcon, QHBoxLayout, \
    QWidget, QSplitter, QVBoxLayout
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

        # add central widget and mainLayout
        centralWidget=QWidget()
        self.setCentralWidget(centralWidget)

        mainLayout=QVBoxLayout(centralWidget)

        splitter = QSplitter(Qt.Horizontal)
        mainLayout.addWidget(splitter)




app=QApplication(sys.argv)
win=ZillowAnalyserWindow()
win.show()
app.exec_()
