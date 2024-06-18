# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextpage_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.setFixedSize(572, 475)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 572, 475))
        self.label_2.setStyleSheet("background-color:#DCF1FE;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 572, 475))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        #self.label.setFont(font)
        #self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.label.setStyleSheet('''
            font-size:28px;
            font-family:cursive;
            color:black;
            font-weight:bold;
            font-style:normal;
        ''')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.visual_drawing = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.visual_drawing.setFont(font)
        self.visual_drawing.setObjectName("visual_drawing")
        self.gridLayout.addWidget(self.visual_drawing, 3, 0, 1, 1)
        self.employee_turnover_forecast = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.employee_turnover_forecast.setFont(font)
        self.employee_turnover_forecast.setObjectName("employee_turnover_forecast")
        self.gridLayout.addWidget(self.employee_turnover_forecast, 2, 0, 1, 1)
        self.manage_employee_information = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.manage_employee_information.setFont(font)
        self.manage_employee_information.setObjectName("manage_employee_information")
        self.gridLayout.addWidget(self.manage_employee_information, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        
        
        script_dir = os.path.dirname(__file__)
        img_path_4 = os.path.join(script_dir, "picture", "p04拷貝.png")
        img_path_4_1 = os.path.join(script_dir, "picture", "p04.png")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 160, 201, 211))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(img_path_4))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-1, 105, 251, 231))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(img_path_4_1))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        
        
        
        
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.layoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "員工管理系統"))
        self.label.setText(_translate("MainWindow", "功能選擇"))
        self.visual_drawing.setText(_translate("MainWindow", "視覺化繪圖"))
        self.employee_turnover_forecast.setText(_translate("MainWindow", "員工離職預測"))
        self.manage_employee_information.setText(_translate("MainWindow", "管理員工資料"))
