# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextpage_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 150, 120, 129))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.manage_employee_information = QtWidgets.QPushButton(self.layoutWidget)
        self.manage_employee_information.setObjectName("manage_employee_information")
        self.gridLayout.addWidget(self.manage_employee_information, 2, 0, 1, 1)
        self.visual_drawing = QtWidgets.QPushButton(self.layoutWidget)
        self.visual_drawing.setObjectName("visual_drawing")
        self.gridLayout.addWidget(self.visual_drawing, 4, 0, 1, 1)
        self.employee_turnover_forecast = QtWidgets.QPushButton(self.layoutWidget)
        self.employee_turnover_forecast.setObjectName("employee_turnover_forecast")
        self.gridLayout.addWidget(self.employee_turnover_forecast, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.manage_employee_information.setText(_translate("MainWindow", "管理員工資料"))
        self.visual_drawing.setText(_translate("MainWindow", "視覺化繪圖"))
        self.employee_turnover_forecast.setText(_translate("MainWindow", "員工離職預測"))
        self.label.setText(_translate("MainWindow", "       功能選擇"))
