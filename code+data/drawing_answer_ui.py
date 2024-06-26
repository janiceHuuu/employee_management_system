# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drawing_answer0612_ui.ui'
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 941)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.previous_page = QtWidgets.QPushButton(self.centralwidget)
        self.previous_page.setGeometry(QtCore.QRect(20, 10, 113, 32))
        self.previous_page.setObjectName("previous_page")
        
        self.selected_field_label = QtWidgets.QLabel(self.centralwidget)
        self.selected_field_label.setGeometry(QtCore.QRect(70, 50, 311, 16))
        self.selected_field_label.setText("")
        self.selected_field_label.setObjectName("selected_field_label")
        
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(60, 110, 701, 441))
        self.graphicsView.setObjectName("graphicsView")

        # Setting background color similar to login_ui.py
        self.centralwidget.setStyleSheet("background-color:#DCF1FE;")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 25))
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
        self.previous_page.setText(_translate("MainWindow", "上一頁"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())