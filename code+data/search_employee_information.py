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
        print(search_criteria)
        
        if not search_criteria:
            self.message.setText("請至少輸入一項搜索條件")
            return
        
        query = "SELECT * FROM PredictionEmployee WHERE " + " AND ".join([f"{key} = ?" for key in search_criteria.keys()])
        
        conn = sqlite3.connect('employee_management.db')
        cursor = conn.cursor()
        cursor.execute(query, tuple(search_criteria.values()))
        
        results = []
        while True:
            chunk = cursor.fetchmany(100)  # 每次加載100行資料
            if not chunk:
                break
            results.extend(chunk)
        
        conn.close()
    
        if not results:
            QMessageBox.warning(self, "No Results", "沒有找到匹配的結果")
        else:
            self.hide()
            from search_answer import SearchAnswerWindow
            self.search_answer_page = SearchAnswerWindow(results)
            self.search_answer_page.show()


    def get_employee_data(self):
        data = {
            "yyyy": self.Year.text(),
            "PerNo": self.PerNo.text(),
            "sex": self.Sex.text(),
            "工作分類": self.Job_classification.text(),
            "職等": self.Grade.text(),
            "廠區代碼": self.FactoryCode.text(),
            "管理層級": self.ManageLevel.text(),
            "歸屬部門": self.BelongingDepartment.text(),
            "工作資歷1": self.WorkQualifications1.text(),
            "工作資歷2": self.WorkQualifications2.text(),
            "工作資歷3": self.WorkQualifications3.text(),
            "工作資歷4": self.WorkQualifications4.text(),
            "工作資歷5": self.WorkQualifications5.text(),
            "是否升遷": self.WhetherPromoted.text(),
            "升遷速度": self.PromotedSpeed.text(),
            "專案時數": self.ProjectHours.text(),
            "專案總數": self.ProjectTotal.text(),
            "當前專案角色": self.CurrentProjectRole.text(),
            "特殊專案佔比": self.ProportionOfSpecialProject.text(),
            "工作地點": self.WorkPlace.text(),
            "訓練時數A": self.TrainingHoursA.text(),
            "訓練時數B": self.TrainingHoursB.text(),
            "訓練時數C": self.TrainingHoursC.text(),
            "生產總額": self.TotalProduction.text(),
            "榮譽數": self.NumberOfHonors.text(),
            "通勤成本": self.CommutingCosts.text(),
            "近三月請假數A": self.Leave3A.text(),
            "近三月請假數B": self.Leave3B.text(),
            "近一年請假數A": self.LeaveYearA.text(),
            "近一年請假數B": self.LeaveYearB.text(),
            "出差數A": self.BusinessTripA.text(),
            "出差數B": self.BusinessTripB.text(),
            "出差集中度": self.BusinessTripConcentration.text(),
            "年度績效等級A": self.AnnualPerformanceGradeA.text(),
            "年度績效等級B": self.AnnualPerformanceGradeB.text(),
            "年度績效等級C": self.AnnualPerformanceGradeC.text(),
            "年齡層級": self.AgeLevel.text(),
            "婚姻狀況": self.MaritalStatus.text(),
            "眷屬量": self.Dependents.text(),
            "年資層級A": self.SeniorityA.text(),
            "年資層級B": self.SeniorityB.text(),
            "年資層級C": self.SeniorityC.text(),
            "任職前工作平均年數": self.AverageYear.text(),
            "最高學歷": self.Education.text(),
            "畢業學校類別": self.School.text(),
            "畢業科系類別": self.Department.text()
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
