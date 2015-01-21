__author__ = 'xuhuan'
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QDesktopServices, QKeySequence
from PyQt5.QtCore import (QDir, QIODevice, QFile, QFileInfo, Qt, QTextStream,
                          QUrl)
from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QAbstractItemView, QApplication, QComboBox,
                             QDialog, QFileDialog, QGridLayout, QHBoxLayout, QHeaderView, QLabel,
                             QProgressDialog, QPushButton, QSizePolicy, QTableWidget,
                             QTableWidgetItem)
from PinB import Ui_MainWindow
import sys


class MainWindows(QtWidgets.QMainWindow, QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindows()
    win.show()
    sys.exit(app.exec_())