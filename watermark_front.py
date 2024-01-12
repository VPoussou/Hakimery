from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic

from PyQt5.QtGui import QPixmap
import os



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(os.path.join(os.path.split(__file__)[0], "steganosaure.ui"), self)