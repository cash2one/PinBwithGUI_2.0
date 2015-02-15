__author__ = 'xuhuan'
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QDesktopServices, QKeySequence
from PyQt5.QtCore import (QDir, QIODevice, QFile, QFileInfo, Qt, QTextStream,
                          QUrl)
from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QAbstractItemView, QApplication, QComboBox,
                             QDialog, QFileDialog, QGridLayout, QHBoxLayout, QHeaderView, QLabel,
                             QProgressDialog, QPushButton, QSizePolicy, QTableWidget,
                             QTableWidgetItem)
from PinBui import Ui_MainWindow
import sys
import pinbiao
from dialog_set_path import Ui_Dialog
import extension


class MainWindows(QtWidgets.QMainWindow, QDialog, Ui_MainWindow):
    WorkPath = ''
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
        self.pushButton_file.clicked.connect(self.select_file_button)
        self.pushButton_fresh.clicked.connect(self.show_files_in_table)
        self.pushButton_action.clicked.connect(self.action_pinbiao)
        self.actionAbout.triggered.connect(self.about)
        self.actionSettingpath.triggered.connect(self.set_WorkPath)
        pinbiao.folder_check(self.output_folder)
        self.get_workpath()
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.show_files_in_table()
        self.tableWidget.cellDoubleClicked.connect(self.select_file_table)

    def about(self):
        QMessageBox.about(self, "关于", "广告<b>拼表</b>工具" + '\n' + 'www.youzu.com')

    def get_workpath(self):
        self.WorkPath = pinbiao.workfolder()
        if self.WorkPath == 'error':
            self.WorkPath = None

    def set_WorkPath(self):
        #dialog = extension.FindDialog(parent=self)
        dialog = SetFolderDialog(parent=self)
        dialog.show()
        #new_path = QFileDialog.getExistingDirectory(self, "工作目录", self.WorkPath)
        #self.WorkPath = new_path
        #return new_path

    def select_file_button(self):
        path = self.WorkPath
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择..", path, "Text Files (*.csv);;All Files (*)",
                                                    options= options)
        if file_name:
            self.display_file_info(file_name)

    def select_file_table(self, row, column):
        item = self.tableWidget.item(row, 0)
        self.display_file_info(self.WorkPath + '/' + item.text())

    def display_file_info(self, file):
        # todo: key error
        if not self.checkBox.isChecked():
            self.file1 = file
            file = pinbiao.getdata(file)
            info = file.info
            self.label_from1.setText(info['file_from'])
            self.label_game1.setText(info['game'])
            self.label_date11.setText(info['begin_date'])
            self.label_date12.setText(info['end_date'])
            #self.checkBox.setChecked(True)
        elif not self.checkBox_2.isChecked():
            self.file2 = file
            file = pinbiao.getdata(file)
            info = file.info
            self.label_from2.setText(info['file_from'])
            self.label_game2.setText(info['game'])
            self.label_date21.setText(info['begin_date'])
            self.label_date22.setText(info['end_date'])
            #self.checkBox_2.setChecked(True)

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
        self.statusbar.showMessage('正在生成结果..')
        result, info = pinbiao.pinbiao(self.file1, self.file2)
        if self.plainTextEdit.toPlainText():
            result_name = self.plainTextEdit.toPlainText()
        else:
            result_name = info['file_from'] + '-' + info['game'] + '-' + info['begin_date'] + '至' + info['end_date']
        self.plainTextEdit.setPlainText(result_name)
        pinbiao.write_csv(result_name, info, result, self.output_folder)
        self.statusbar.showMessage('拼表成功!', 6000)
        self.plainTextEdit.clear()


class SetFolderDialog(QDialog, Ui_Dialog):
    folder = ''
    WorkPath = 'D:\workstation'
    def __init__(self, parent=None):
        super(SetFolderDialog, self).__init__(parent)
        self.setupUi(self) # 不写这个就会只有框没有界面内容
        self.setWindowTitle("设置路径")
        self.lineEdit.setText(self.WorkPath)
        self.pushButton.clicked.connect(self.select_folder)
        self.accepted.connect(self.get_folder)

    def select_folder(self):
        self.folder = QFileDialog.getExistingDirectory(self, "工作目录", self.WorkPath)
        self.lineEdit.setText(self.folder)

    def get_folder(self):
        return self.lineEdit.text()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindows()
    win.show()
    sys.exit(app.exec_())