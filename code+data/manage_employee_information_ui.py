# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_employee_information_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.previous_page = QtWidgets.QPushButton(self.centralwidget)
        self.previous_page.setGeometry(QtCore.QRect(10, 20, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.previous_page.setFont(font)
        self.previous_page.setObjectName("previous_page")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 50, 611, 488))
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TotalProduction = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.TotalProduction.setFont(font)
        self.TotalProduction.setObjectName("TotalProduction")
        self.gridLayout.addWidget(self.TotalProduction, 8, 3, 1, 1)
        self.labeln = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.labeln.setFont(font)
        self.labeln.setObjectName("labeln")
        self.gridLayout.addWidget(self.labeln, 8, 2, 1, 1)
        self.Dependents = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Dependents.setFont(font)
        self.Dependents.setObjectName("Dependents")
        self.gridLayout.addWidget(self.Dependents, 8, 5, 1, 1)
        self.TrainingHoursC = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.TrainingHoursC.setFont(font)
        self.TrainingHoursC.setObjectName("TrainingHoursC")
        self.gridLayout.addWidget(self.TrainingHoursC, 7, 3, 1, 1)
        self.MaritalStatus = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.MaritalStatus.setFont(font)
        self.MaritalStatus.setObjectName("MaritalStatus")
        self.gridLayout.addWidget(self.MaritalStatus, 7, 5, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 7, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 7, 2, 1, 1)
        self.AgeLevel = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.AgeLevel.setFont(font)
        self.AgeLevel.setObjectName("AgeLevel")
        self.gridLayout.addWidget(self.AgeLevel, 6, 5, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 12, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 13, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.WorkQualifications3 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.WorkQualifications3.setFont(font)
        self.WorkQualifications3.setObjectName("WorkQualifications3")
        self.gridLayout.addWidget(self.WorkQualifications3, 10, 1, 1, 1)
        self.WhetherPromoted = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.WhetherPromoted.setFont(font)
        self.WhetherPromoted.setObjectName("WhetherPromoted")
        self.gridLayout.addWidget(self.WhetherPromoted, 13, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.WorkQualifications1 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.WorkQualifications1.setFont(font)
        self.WorkQualifications1.setObjectName("WorkQualifications1")
        self.gridLayout.addWidget(self.WorkQualifications1, 8, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 14, 0, 1, 1)
        self.Sex = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Sex.setFont(font)
        self.Sex.setObjectName("Sex")
        self.gridLayout.addWidget(self.Sex, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 13, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        self.WorkQualifications4 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.WorkQualifications4.setFont(font)
        self.WorkQualifications4.setObjectName("WorkQualifications4")
        self.gridLayout.addWidget(self.WorkQualifications4, 11, 1, 1, 1)
        self.ManageLevel = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.ManageLevel.setFont(font)
        self.ManageLevel.setObjectName("ManageLevel")
        self.gridLayout.addWidget(self.ManageLevel, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.gridLayout.addWidget(self.label_73, 7, 0, 1, 1)
        self.FactoryCode = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.FactoryCode.setFont(font)
        self.FactoryCode.setObjectName("FactoryCode")
        self.gridLayout.addWidget(self.FactoryCode, 5, 1, 1, 1)
        self.Grade = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Grade.setFont(font)
        self.Grade.setObjectName("Grade")
        self.gridLayout.addWidget(self.Grade, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.Job_classification = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Job_classification.setFont(font)
        self.Job_classification.setObjectName("Job_classification")
        self.gridLayout.addWidget(self.Job_classification, 3, 1, 1, 1)
        self.WorkQualifications2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.WorkQualifications2.setFont(font)
        self.WorkQualifications2.setObjectName("WorkQualifications2")
        self.gridLayout.addWidget(self.WorkQualifications2, 9, 1, 1, 1)
        self.WorkQualifications5 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.WorkQualifications5.setFont(font)
        self.WorkQualifications5.setObjectName("WorkQualifications5")
        self.gridLayout.addWidget(self.WorkQualifications5, 12, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 14, 2, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.gridLayout.addWidget(self.label_67, 11, 4, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.gridLayout.addWidget(self.label_69, 12, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.BusinessTripA = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.BusinessTripA.setFont(font)
        self.BusinessTripA.setObjectName("BusinessTripA")
        self.gridLayout.addWidget(self.BusinessTripA, 0, 5, 1, 1)
        self.ProjectHours = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.ProjectHours.setFont(font)
        self.ProjectHours.setObjectName("ProjectHours")
        self.gridLayout.addWidget(self.ProjectHours, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 2, 1, 1)
        self.ProjectTotal = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.ProjectTotal.setFont(font)
        self.ProjectTotal.setObjectName("ProjectTotal")
        self.gridLayout.addWidget(self.ProjectTotal, 1, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 0, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 2, 1, 1)
        self.PerNo = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.PerNo.setFont(font)
        self.PerNo.setObjectName("PerNo")
        self.gridLayout.addWidget(self.PerNo, 1, 1, 1, 1)
        self.BusinessTripB = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.BusinessTripB.setFont(font)
        self.BusinessTripB.setObjectName("BusinessTripB")
        self.gridLayout.addWidget(self.BusinessTripB, 1, 5, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 1, 4, 1, 1)
        self.Year = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Year.setFont(font)
        self.Year.setObjectName("Year")
        self.gridLayout.addWidget(self.Year, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.SeniorityB = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.SeniorityB.setFont(font)
        self.SeniorityB.setObjectName("SeniorityB")
        self.gridLayout.addWidget(self.SeniorityB, 10, 5, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.gridLayout.addWidget(self.label_68, 10, 4, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 9, 2, 1, 1)
        self.PromotedSpeed = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.PromotedSpeed.setFont(font)
        self.PromotedSpeed.setObjectName("PromotedSpeed")
        self.gridLayout.addWidget(self.PromotedSpeed, 14, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 10, 2, 1, 1)
        self.CommutingCosts = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.CommutingCosts.setFont(font)
        self.CommutingCosts.setObjectName("CommutingCosts")
        self.gridLayout.addWidget(self.CommutingCosts, 10, 3, 1, 1)
        self.NumberOfHonors = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.NumberOfHonors.setFont(font)
        self.NumberOfHonors.setObjectName("NumberOfHonors")
        self.gridLayout.addWidget(self.NumberOfHonors, 9, 3, 1, 1)
        self.SeniorityA = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.SeniorityA.setFont(font)
        self.SeniorityA.setObjectName("SeniorityA")
        self.gridLayout.addWidget(self.SeniorityA, 9, 5, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.gridLayout.addWidget(self.label_66, 9, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 11, 2, 1, 1)
        self.Department = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Department.setFont(font)
        self.Department.setObjectName("Department")
        self.gridLayout.addWidget(self.Department, 15, 5, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.gridLayout.addWidget(self.label_72, 15, 4, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.gridLayout.addWidget(self.label_70, 13, 4, 1, 1)
        self.Education = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Education.setFont(font)
        self.Education.setObjectName("Education")
        self.gridLayout.addWidget(self.Education, 13, 5, 1, 1)
        self.LeaveYearB = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.LeaveYearB.setFont(font)
        self.LeaveYearB.setObjectName("LeaveYearB")
        self.gridLayout.addWidget(self.LeaveYearB, 14, 3, 1, 1)
        self.Leave3B = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Leave3B.setFont(font)
        self.Leave3B.setObjectName("Leave3B")
        self.gridLayout.addWidget(self.Leave3B, 12, 3, 1, 1)
        self.LeaveYearA = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.LeaveYearA.setFont(font)
        self.LeaveYearA.setObjectName("LeaveYearA")
        self.gridLayout.addWidget(self.LeaveYearA, 13, 3, 1, 1)
        self.School = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.School.setFont(font)
        self.School.setObjectName("School")
        self.gridLayout.addWidget(self.School, 14, 5, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.gridLayout.addWidget(self.label_71, 14, 4, 1, 1)
        self.AverageYear = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.AverageYear.setFont(font)
        self.AverageYear.setObjectName("AverageYear")
        self.gridLayout.addWidget(self.AverageYear, 12, 5, 1, 1)
        self.Leave3A = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Leave3A.setFont(font)
        self.Leave3A.setObjectName("Leave3A")
        self.gridLayout.addWidget(self.Leave3A, 11, 3, 1, 1)
        self.SeniorityC = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.SeniorityC.setFont(font)
        self.SeniorityC.setObjectName("SeniorityC")
        self.gridLayout.addWidget(self.SeniorityC, 11, 5, 1, 1)
        self.ProportionOfSpecialProject = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.ProportionOfSpecialProject.setFont(font)
        self.ProportionOfSpecialProject.setObjectName("ProportionOfSpecialProject")
        self.gridLayout.addWidget(self.ProportionOfSpecialProject, 3, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 3, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 2, 4, 1, 1)
        self.CurrentProjectRole = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.CurrentProjectRole.setFont(font)
        self.CurrentProjectRole.setObjectName("CurrentProjectRole")
        self.gridLayout.addWidget(self.CurrentProjectRole, 2, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 2, 1, 1)
        self.BusinessTripConcentration = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.BusinessTripConcentration.setFont(font)
        self.BusinessTripConcentration.setObjectName("BusinessTripConcentration")
        self.gridLayout.addWidget(self.BusinessTripConcentration, 2, 5, 1, 1)
        self.AnnualPerformanceGradeC = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.AnnualPerformanceGradeC.setFont(font)
        self.AnnualPerformanceGradeC.setObjectName("AnnualPerformanceGradeC")
        self.gridLayout.addWidget(self.AnnualPerformanceGradeC, 5, 5, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 4, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 3, 4, 1, 1)
        self.TrainingHoursA = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.TrainingHoursA.setFont(font)
        self.TrainingHoursA.setObjectName("TrainingHoursA")
        self.gridLayout.addWidget(self.TrainingHoursA, 5, 3, 1, 1)
        self.BelongingDepartment = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.BelongingDepartment.setFont(font)
        self.BelongingDepartment.setObjectName("BelongingDepartment")
        self.gridLayout.addWidget(self.BelongingDepartment, 7, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 4, 4, 1, 1)
        self.AnnualPerformanceGradeB = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.AnnualPerformanceGradeB.setFont(font)
        self.AnnualPerformanceGradeB.setObjectName("AnnualPerformanceGradeB")
        self.gridLayout.addWidget(self.AnnualPerformanceGradeB, 4, 5, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 5, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 5, 2, 1, 1)
        self.AnnualPerformanceGradeA = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.AnnualPerformanceGradeA.setFont(font)
        self.AnnualPerformanceGradeA.setObjectName("AnnualPerformanceGradeA")
        self.gridLayout.addWidget(self.AnnualPerformanceGradeA, 3, 5, 1, 1)
        self.TrainingHoursB = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.TrainingHoursB.setFont(font)
        self.TrainingHoursB.setObjectName("TrainingHoursB")
        self.gridLayout.addWidget(self.TrainingHoursB, 6, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 6, 2, 1, 1)
        self.WorkPlace = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.WorkPlace.setFont(font)
        self.WorkPlace.setObjectName("WorkPlace")
        self.gridLayout.addWidget(self.WorkPlace, 4, 3, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 8, 4, 1, 1)
        self.Label_n = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.Label_n.setFont(font)
        self.Label_n.setObjectName("Label_n")
        self.gridLayout.addWidget(self.Label_n, 6, 4, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(530, 550, 382, 32))
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.layoutWidget_2.setFont(font)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.delet_employee_information = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.delet_employee_information.setFont(font)
        self.delet_employee_information.setObjectName("delet_employee_information")
        self.gridLayout_2.addWidget(self.delet_employee_information, 0, 0, 1, 1)
        self.update_employee_information = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.update_employee_information.setFont(font)
        self.update_employee_information.setObjectName("update_employee_information")
        self.gridLayout_2.addWidget(self.update_employee_information, 0, 1, 1, 1)
        self.add_employee_information = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.add_employee_information.setFont(font)
        self.add_employee_information.setObjectName("add_employee_information")
        self.gridLayout_2.addWidget(self.add_employee_information, 0, 2, 1, 1)
        self.success = QtWidgets.QLabel(self.centralwidget)
        self.success.setGeometry(QtCore.QRect(140, 550, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Heiti TC")
        font.setPointSize(14)
        self.success.setFont(font)
        self.success.setText("")
        self.success.setObjectName("success")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-80, -15, 1521, 881))
        self.label_3.setStyleSheet("background-color:#DCF1FE;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(750, 30, 151, 151))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("../../../../Downloads/p04拷貝2.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(0, 500, 111, 111))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("../../../../Downloads/ppppp.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setObjectName("label_36")
        self.label_3.raise_()
        self.previous_page.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.success.raise_()
        self.label_22.raise_()
        self.label_36.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.previous_page.setText(_translate("MainWindow", "上一頁"))
        self.labeln.setText(_translate("MainWindow", "生產總額："))
        self.label_37.setText(_translate("MainWindow", "婚姻狀況："))
        self.label_21.setText(_translate("MainWindow", "訓練時數C："))
        self.label_28.setText(_translate("MainWindow", "近三月請假數B："))
        self.label_27.setText(_translate("MainWindow", "近一年請假數A："))
        self.label_8.setText(_translate("MainWindow", "管理層級："))
        self.label_11.setText(_translate("MainWindow", "工作資歷3："))
        self.label_25.setText(_translate("MainWindow", "升遷速度："))
        self.label_9.setText(_translate("MainWindow", "工作資歷1："))
        self.label_10.setText(_translate("MainWindow", "工作資歷2："))
        self.label_24.setText(_translate("MainWindow", "是否升遷："))
        self.label_12.setText(_translate("MainWindow", "工作資歷4："))
        self.label_4.setText(_translate("MainWindow", "sex："))
        self.label_73.setText(_translate("MainWindow", "歸屬部門："))
        self.label_7.setText(_translate("MainWindow", "廠區代碼："))
        self.label_13.setText(_translate("MainWindow", "工作資歷5："))
        self.label_5.setText(_translate("MainWindow", "工作分類："))
        self.label_6.setText(_translate("MainWindow", "職等："))
        self.label_29.setText(_translate("MainWindow", "近一年請假數B："))
        self.label_67.setText(_translate("MainWindow", "年資層級C："))
        self.label_69.setText(_translate("MainWindow", "任職前工作平均年數："))
        self.label_2.setText(_translate("MainWindow", "PerNo："))
        self.label_14.setText(_translate("MainWindow", "專案時數："))
        self.label_30.setText(_translate("MainWindow", "出差數A："))
        self.label_15.setText(_translate("MainWindow", "專案總數："))
        self.label_32.setText(_translate("MainWindow", "出差數B："))
        self.label.setText(_translate("MainWindow", "year："))
        self.label_68.setText(_translate("MainWindow", "年資層級B："))
        self.label_23.setText(_translate("MainWindow", "榮譽數："))
        self.label_39.setText(_translate("MainWindow", "通勤成本："))
        self.label_66.setText(_translate("MainWindow", "年資層級A："))
        self.label_26.setText(_translate("MainWindow", "近三月請假數A："))
        self.label_72.setText(_translate("MainWindow", "畢業科系類別："))
        self.label_70.setText(_translate("MainWindow", "最高學歷："))
        self.label_71.setText(_translate("MainWindow", "畢業學校類別："))
        self.label_17.setText(_translate("MainWindow", "特殊專案佔比："))
        self.label_31.setText(_translate("MainWindow", "出差集中度："))
        self.label_16.setText(_translate("MainWindow", "當前專案角色："))
        self.label_18.setText(_translate("MainWindow", "工作地點："))
        self.label_33.setText(_translate("MainWindow", "年度績效等級A："))
        self.label_34.setText(_translate("MainWindow", "年度績效等級B："))
        self.label_35.setText(_translate("MainWindow", "年度績效等級C："))
        self.label_19.setText(_translate("MainWindow", "訓練時數A："))
        self.label_20.setText(_translate("MainWindow", "訓練時數B："))
        self.label_38.setText(_translate("MainWindow", "眷屬量："))
        self.Label_n.setText(_translate("MainWindow", "年齡層級："))
        self.delet_employee_information.setText(_translate("MainWindow", "刪除員工資料"))
        self.update_employee_information.setText(_translate("MainWindow", "更新員工資料"))
        self.add_employee_information.setText(_translate("MainWindow", "新增員工資料"))
