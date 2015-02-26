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


class MainWindows(QtWidgets.QMainWindow, QDialog, Ui_MainWindow):
    output_folder = '拼表结果'
    file1 = ''
    file2 = ''
    isFile1Busy = False
    isFile2Busy = False
    MOD = None

    def __init__(self, cwd, parent=None):
        self.work_folder = cwd
        super(MainWindows, self).__init__(parent)
        self.setupUi(self)
        # self.errorMessageDialog = QErrorMessage(self)
        self.pushButton_file.clicked.connect(self.select_file_button)
        self.pushButton_fresh.clicked.connect(self.show_files_in_table)
        self.pushButton_action.clicked.connect(self.action_pinbiao)
        self.actionAbout.triggered.connect(self.about)
        self.actionSettingpath.triggered.connect(self.set_work_folder)
        pinbiao.folder_check(self.output_folder)
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

    def set_work_folder(self):
        dialog = SetFolderDialog(self.work_folder, parent=self)
        dialog.show()
        if dialog.exec_():
            self.work_folder = dialog.work_folder

    def select_file_button(self):
        path = self.work_folder
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
        try:
            if not self.checkBox.isChecked():
                self.file1 = file
                file = pinbiao.getdata(file)
                if isinstance(file, str):
                    QMessageBox.information(self, "错误", file)
                    self.file1 = ''
                    return 0
                info = file.info
                self.label_from1.setText(info['file_from'])
                self.label_game1.setText(info['game'])
                self.label_date11.setText(info['begin_date'])
                self.label_date12.setText(info['end_date'])
                #self.checkBox.setChecked(True)
            elif not self.checkBox_2.isChecked():
                self.file2 = file
                file = pinbiao.getdata(file)
                if isinstance(file, str):
                    QMessageBox.information(self, "错误", file)
                    self.file2 = ''
                    return 0
                info = file.info
                self.label_from2.setText(info['file_from'])
                self.label_game2.setText(info['game'])
                self.label_date21.setText(info['begin_date'])
                self.label_date22.setText(info['end_date'])
                #self.checkBox_2.setChecked(True)
        except Exception as error_message:
            QMessageBox.information(self, "错误", str(error_message))

    def show_files_in_table(self):
        self.tableWidget.setRowCount(0)
        files = pinbiao.file_list(self.work_folder)
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
        if self.lineEdit.text():
            result_name = self.lineEdit.text()
        else:
            result_name = info['file_from'] + '-' + info['game'] + '-' + info['begin_date'] + '至' + info['end_date']
        self.lineEdit.text(result_name)
        pinbiao.write_csv(result_name, info, result, self.output_folder)
        self.statusbar.showMessage('拼表成功!', 6000)
        self.lineEdit.clear()


class SetFolderDialog(QDialog, Ui_Dialog):
    new_folder = ''

    def __init__(self, cwd, parent=None):
        self.work_folder = cwd
        super(SetFolderDialog, self).__init__(parent)
        self.setupUi(self)  # 不写这个就会只有框没有界面内容
        self.setWindowTitle("设置路径")
        self.lineEdit.setText(self.work_folder)
        self.pushButton.clicked.connect(self.open_select_folder)
        self.accepted.connect(self.get_folder)

    def open_select_folder(self):
        self.new_folder = QFileDialog.getExistingDirectory(self, "工作目录", self.work_folder)
        self.lineEdit.setText(self.new_folder)

    def get_folder(self):
        try:
            pinbiao.folder_check(self.lineEdit.text())
            self.work_folder = self.lineEdit.text()
        except:
            return self.work_folder

if __name__ == '__main__':
    work_folder = pinbiao.get_work_folder()
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindows(work_folder)
    win.show()
    sys.exit(app.exec_())