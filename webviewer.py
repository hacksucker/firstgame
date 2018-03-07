import os
import sys
import time as tm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QtWidgets.QApplication(sys.argv)
splash_pix = QtGui.QPixmap("map.jpg")
splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
splash.setMask(splash_pix.mask())
splash.show()
tm.sleep(10)
splash.finish(gui)