import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from search_employee_information_ui import Ui_MainWindow as Ui_SearchEmployeeInformationWindow
import sqlite3

class SearchEmployeeInformationWindow(QMainWindow, Ui_SearchEmployeeInformationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.search.clicked.connect(self.search_employee)
        self.previous_page.clicked.connect(self.go_to_previous_page)

    def search_employee(self):
        data = self.get_employee_data()
        search_criteria = {key: value for key, value in data.items() if value}
        
        if not search_criteria:
            self.message.setText("請至少輸入一項搜索條件")  # 在 QLabel 中顯示錯誤訊息
            self.messageLabel.setText("Incorrect username or password.\nPlease try again.")
            return
        
        query = "SELECT * FROM employees WHERE " + " AND ".join([f"{key} = ?" for key in search_criteria.keys()])
        conn = sqlite3.connect('employee_management.db')
        cursor = conn.cursor()
        cursor.execute(query, tuple(search_criteria.values()))
        results = cursor.fetchall()
        conn.close()
    
        if not results:
            QMessageBox.warning(self, "No Results", "沒有找到匹配的結果")
        else:
            self.hide()  # 隱藏當前窗口
            from search_answer import SearchAnswerWindow
            self.search_answer_page = SearchAnswerWindow(results)
            self.search_answer_page.show()


    def get_employee_data(self):
        data = {
            "PerStatus": self.PerStatus.text(),
            "PerNo": self.PerNo.text(),
            "Sex": self.Sex.text(),
            "Job_classification": self.Job_classification.text(),
            "Grade": self.Grade.text(),
            "FactoryCode": self.FactoryCode.text(),
            "ManageLevel": self.ManageLevel.text(),
            "BelongingDepartment": self.BelongingDepartment.text(),
            "WorkQualifications1": self.WorkQualifications1.text(),
            "WorkQualifications2": self.WorkQualifications2.text(),
            "WorkQualifications3": self.WorkQualifications3.text(),
            "WorkQualifications4": self.WorkQualifications4.text(),
            "WorkQualifications5": self.WorkQualifications5.text(),
            "WhetherPromoted": self.WhetherPromoted.text(),
            "PromotedSpeed": self.PromotedSpeed.text(),
            "ProjectHours": self.ProjectHours.text(),
            "ProjectTotal": self.ProjectTotal.text(),
            "CurrentProjectRole": self.CurrentProjectRole.text(),
            "ProportionOfSpecialProject": self.ProportionOfSpecialProject.text(),
            "WorkPlace": self.WorkPlace.text(),
            "TrainingHoursA": self.TrainingHoursA.text(),
            "TrainingHoursB": self.TrainingHoursB.text(),
            "TrainingHoursC": self.TrainingHoursC.text(),
            "TotalProduction": self.TotalProduction.text(),
            "NumberOfHonors": self.NumberOfHonors.text(),
            "CommutingCosts": self.CommutingCosts.text(),
            "Leave3A": self.Leave3A.text(),
            "Leave3B": self.Leave3B.text(),
            "LeaveYearA": self.LeaveYearA.text(),
            "LeaveYearB": self.LeaveYearB.text(),
            "BusinessTripA": self.BusinessTripA.text(),
            "BusinessTripB": self.BusinessTripB.text(),
            "BusinessTripConcentration": self.BusinessTripConcentration.text(),
            "AnnualPerformanceGradeA": self.AnnualPerformanceGradeA.text(),
            "AnnualPerformanceGradeB": self.AnnualPerformanceGradeB.text(),
            "AnnualPerformanceGradeC": self.AnnualPerformanceGradeC.text(),
            "AgeLevel": self.AgeLevel.text(),
            "MaritalStatus": self.MaritalStatus.text(),
            "Dependents": self.Dependents.text(),
            "SeniorityA": self.SeniorityA.text(),
            "SeniorityB": self.SeniorityB.text(),
            "SeniorityC": self.SeniorityC.text(),
            "AverageYear": self.AverageYear.text(),
            "Education": self.Education.text(),
            "School": self.School.text(),
            "Department": self.Department.text()
        }
        return data

    def go_to_previous_page(self):
        from nextpage import NextPageWindow
        self.next_page = NextPageWindow()
        self.next_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchEmployeeInformationWindow()
    window.show()
    sys.exit(app.exec_())
