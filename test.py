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
    output_folder = '拼表结果'
    file1 = ''
    file2 = ''
    isFile1Busy = False
    isFile2Busy = False
    MOD = None

    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)
        # self.errorMessageDialog = QErrorMessage(self)
        self.pushButton_file.clicked.connect(self.select_file)
        self.pushButton_fresh.clicked.connect(self.show_files_in_table)
        self.pushButton_action.clicked.connect(self.action_pinbiao)
        pinbiao.folder_check(self.output_folder)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.show_files_in_table()
        # self.file_list_table.cellActivated.connect(self.open_file_of_item)
        # self.file_list_table.cellPressed.connect(self.open_file_of_item)
        # self.tableView.cellClicked.connect(self.show_file_info)
        # self.tableView.cellEntered.connect(self.open_file_of_item)
        # self.tableView.cellDoubleClicked.connect(self.doubleclick_to_add_file)

    def select_file(self):
        # open_path = self.directory_path.currentText()
        path = self.WorkPath
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择..", 'C:/Users/xuhuan/Downloads', "Text Files (*.csv);;All Files (*)",
                                                    options= options)
        if file_name:
            self.display_file_info(file_name)

    def display_file_info(self, file):
        # todo: key error
        if not self.isFile1Busy:
            file = pinbiao.getdata(file)
            info = file.info
            self.label_from1.setText(info['file_from'])
            self.label_game1.setText(info['game'])
            self.label_date11.setText(info['begin_date'])
            self.label_date12.setText(info['end_date'])
            self.isFile1Busy = True
            self.file1 = file
        elif not self.isFile2Busy:
            file = pinbiao.getdata(file)
            info = file.info
            self.label_from2.setText(info['file_from'])
            self.label_game2.setText(info['game'])
            self.label_date21.setText(info['begin_date'])
            self.label_date22.setText(info['end_date'])
            self.isFile2Busy = True
            self.file2 = file

    def show_files_in_table(self):
        self.tableWidget.setRowCount(0)
        files = pinbiao.file_list(self.WorkPath)
        for fn in files:
            # todo: 绝对？
            fileNameItem = QTableWidgetItem(fn)
            fileNameItem.setFlags(fileNameItem.flags() ^ Qt.ItemIsEditable)
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, fileNameItem)

    def action_pinbiao(self):
        result, info = pinbiao.pinbiao(self.file1, self.file2)
        result_name = info['file_from'] + '-' + info['game'] + '-' + info['begin_date'] + '至' + info['end_date']
        pinbiao.write_csv(result_name, self.output_folder)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindows()
    win.show()
    sys.exit(app.exec_())