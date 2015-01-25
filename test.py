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
    WorkPath = 'C:/Users/xuhuan/Downloads'

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)
        # self.errorMessageDialog = QErrorMessage(self)
        self.pushButton_file.clicked.connect(self.select_file())
        #self.table_setting()
        #self.display_file_info()

    def select_file(self):
        # open_path = self.directory_path.currentText()
        path = self.WorkPath
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择..", 'C:/Users/xuhuan/Downloads', "Text Files (*.csv);;All Files (*)",
                                                    options= options)
        if file_name:
            self.display_file_info(file_name)
    # self.openFileNameLabel.setText(fileName)

    def display_file_info(self, file):
        file = pinbiao.getdata(file)
        info = file.info
        # todo: key error
        self.label_from1.setText(info['file_from'])
        self.label_game1.setText(info['game'])
        self.label_date11.setText(info['begin_date'])
        self.label_date12.setText(info['end_date'])

    def short_name(self):
        pass

    def display_files_name(self):
        files_list = get_files(working_path)
        for i in files_list:
            i = self.short_name(i)
        k = 0
        for i in files_list:
            self.file_name_
            #{} = QLabel()
            self.file_name.setText(i)

    def table_setting(self):
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        # self.file_list_table.cellActivated.connect(self.open_file_of_item)
        # self.file_list_table.cellPressed.connect(self.open_file_of_item)
        # self.tableView.cellClicked.connect(self.show_file_info)
        # self.tableView.cellEntered.connect(self.open_file_of_item)
        # self.tableView.cellDoubleClicked.connect(self.doubleclick_to_add_file)

    #获取工作路径文件并调用show_file()函数在表格展示
    def show_files_of_path(self, path):
        #表格展示函数
        def show_files_in_table(fs):
            for fn in fs:
                # todo: 绝对？
                f = QFile(self.currentDir.absoluteFilePath(fn))
                size = QFileInfo(f).size()
                fileNameItem = QTableWidgetItem(fn)
                fileNameItem.setFlags(fileNameItem.flags() ^ Qt.ItemIsEditable)
                #sizeItem = QTableWidgetItem("%d KB" % (int((size + 1023) / 1024)))
                #sizeItem.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                #sizeItem.setFlags(sizeItem.flags() ^ Qt.ItemIsEditable)

                row = self.tableView.rowCount()
                self.tableView.insertRow(row)
                self.tableView.setItem(row, 0, fileNameItem)
                #self.file_list_table.setItem(row, 1, sizeItem)
                #self.filesFoundLabel.setText("%d file(s) found (Double click on a file to open it)" % len(files))

        self.tableView.setRowCount(0)
        #self.currentDir = QDir(path)
        #files = self.currentDir.entryList(QDir.Files | QDir.NoSymLinks)
        #path = "C:\Users\xuhuan\Downloads"
        path = 'C:/Users/xuhuan/Downloads'
        files = pinbiao.file_list(path)
        print(files[1])
        show_files_in_table(files)

'''
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