# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PinB.ui'
#
# Created: Thu Jan 29 00:49:38 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 550)
        MainWindow.setMinimumSize(QtCore.QSize(310, 550))
        MainWindow.setMaximumSize(QtCore.QSize(700, 550))
        MainWindow.setBaseSize(QtCore.QSize(700, 550))
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file.setGeometry(QtCore.QRect(30, 15, 101, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_file.sizePolicy().hasHeightForWidth())
        self.pushButton_file.setSizePolicy(sizePolicy)
        self.pushButton_file.setStatusTip("")
        self.pushButton_file.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_file.setObjectName("pushButton_file")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 450, 321, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_action = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_action.setGeometry(QtCore.QRect(400, 450, 271, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_action.sizePolicy().hasHeightForWidth())
        self.pushButton_action.setSizePolicy(sizePolicy)
        self.pushButton_action.setObjectName("pushButton_action")
        self.pushButton_fresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fresh.setGeometry(QtCore.QRect(260, 15, 91, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_fresh.sizePolicy().hasHeightForWidth())
        self.pushButton_fresh.setSizePolicy(sizePolicy)
        self.pushButton_fresh.setObjectName("pushButton_fresh")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(400, 13, 270, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(315, 167, 21, 19))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_2.setGeometry(QtCore.QRect(100, 20, 161, 161))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_from1 = QtWidgets.QLabel(self.splitter_2)
        self.label_from1.setText("")
        self.label_from1.setObjectName("label_from1")
        self.label_game1 = QtWidgets.QLabel(self.splitter_2)
        self.label_game1.setText("")
        self.label_game1.setObjectName("label_game1")
        self.label_date11 = QtWidgets.QLabel(self.splitter_2)
        self.label_date11.setText("")
        self.label_date11.setObjectName("label_date11")
        self.label_date12 = QtWidgets.QLabel(self.splitter_2)
        self.label_date12.setText("")
        self.label_date12.setObjectName("label_date12")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 45, 161))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 240, 270, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(315, 167, 21, 19))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_3.setGeometry(QtCore.QRect(10, 20, 45, 161))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_5 = QtWidgets.QLabel(self.splitter_3)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.splitter_3)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.splitter_3)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.splitter_3)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_4.setGeometry(QtCore.QRect(100, 20, 161, 161))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_from2 = QtWidgets.QLabel(self.splitter_4)
        self.label_from2.setText("")
        self.label_from2.setObjectName("label_from2")
        self.label_game2 = QtWidgets.QLabel(self.splitter_4)
        self.label_game2.setText("")
        self.label_game2.setObjectName("label_game2")
        self.label_date21 = QtWidgets.QLabel(self.splitter_4)
        self.label_date21.setText("")
        self.label_date21.setObjectName("label_date21")
        self.label_date22 = QtWidgets.QLabel(self.splitter_4)
        self.label_date22.setText("")
        self.label_date22.setObjectName("label_date22")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 321, 381))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.verticalHeader().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettingpath = QtWidgets.QAction(MainWindow)
        self.actionSettingpath.setObjectName("actionSettingpath")
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.actionSettingpath)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "拼表"))
        self.pushButton_file.setText(_translate("MainWindow", "文件"))
        self.pushButton_action.setText(_translate("MainWindow", "拼表"))
        self.pushButton_fresh.setText(_translate("MainWindow", "刷新"))
        self.groupBox.setTitle(_translate("MainWindow", "表格1"))
        self.label.setText(_translate("MainWindow", "来源："))
        self.label_2.setText(_translate("MainWindow", "游戏："))
        self.label_3.setText(_translate("MainWindow", "日期："))
        self.groupBox_2.setTitle(_translate("MainWindow", "表格2"))
        self.label_5.setText(_translate("MainWindow", "来源："))
        self.label_6.setText(_translate("MainWindow", "游戏："))
        self.label_7.setText(_translate("MainWindow", "日期："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文件名"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSettingpath.setText(_translate("MainWindow", "设置路径"))
        self.actionSettingpath.setShortcut(_translate("MainWindow", "Ctrl+S"))

import image_rc
