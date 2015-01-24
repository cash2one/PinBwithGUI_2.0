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
import pinbiao


class MainWindows(QtWidgets.QMainWindow, QDialog, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)
        # self.errorMessageDialog = QErrorMessage(self)
        self.pushButton_file.clicked.connect(self.set_file)


    def set_file(self):
        # open_path = self.directory_path.currentText()
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileNames()",
                                                  'C:\Program Files (x86)', "Text Files (*.csv);;All Files (*)",
                                                  options=options)
        if fileName:
            pass

    # self.openFileNameLabel.setText(fileName)
'''

    def short_name(self):
        pass
        # todo


    def display_files_name(self):
        files_list = get_files(working_path)
        for i in files_list:
            i = self.short_name(i)
        k = 0
        for i in files_list:
            self.file_name_
            {} = QLabel()
            self.file_name.setText(i)


    def errorMessage(self):
        self.errorMessageDialog.showMessage("This dialog shows and remembers "
                                            "error messages. If the checkbox is checked (as it is by "
                                            "default), the shown message will be shown again, but if the "
                                            "user unchecks the box the message will not appear again if "
                                            "QErrorMessage.showMessage() is called with the same message.")
        self.errorLabel.setText("If the box is unchecked, the message won't "
                                "appear again.")
'''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindows()
    win.show()
    sys.exit(app.exec_())