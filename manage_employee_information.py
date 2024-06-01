import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from manage_employee_information_ui import Ui_MainWindow as Ui_ManageEmployeeInformationWindow
import sqlite3

class ManageEmployeeInformationWindow(QMainWindow, Ui_ManageEmployeeInformationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_employee_information.clicked.connect(self.add_employee)
        self.update_employee_information.clicked.connect(self.update_employee)
        self.delet_employee_information.clicked.connect(self.delete_employee)
        self.previous_page.clicked.connect(self.go_to_previous_page)

    def get_employee_data(self):
        data = {
            'Answer': 3,
            "Year": self.Year.text(),
            "PerNo": self.PerNo.text(),
            "PerStatus": self.PerStatus.text(),
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
    
    def clear_text_fields(self):
            # 循环清除所有文本框的文本
            for widget in self.findChildren(QLineEdit):
                widget.clear()
    
    def add_employee(self):
        data = self.get_employee_data()
        
        # 檢查所有欄目是否為填寫
        if any(value == "" for value in data.values()):
            self.success.setText("因有欄目未被填寫或員工在職狀態、編號異常\n，故加入資料庫失敗，請重新填寫")
            return
        
        # 檢查 PerStatus 是否為 0
        if data['PerStatus'] == "0":
            self.success.setText("因有欄目未被填寫或員工在職狀態、編號異常\n，故加入資料庫失敗，請重新填寫")
            return
        
        conn = sqlite3.connect('employee_management.db')
        cursor = conn.cursor()
        
        # 檢查 PerNo 是否存在於資料庫
        cursor.execute('SELECT PerNo FROM employees WHERE PerNo = ?', (data['PerNo'],))
        if cursor.fetchone() is not None:
            self.success.setText("因有欄目未被填寫或員工在職狀態、編號異常\n，故加入資料庫失敗，請重新填寫")
            conn.close()
            return
    
        try:
            cursor.execute('''
            INSERT INTO employees VALUES (
                :Answer, :Year, :PerNo, :PerStatus, :Sex, :Job_classification, :Grade, :FactoryCode,
                :ManageLevel, :BelongingDepartment, :WorkQualifications1, :WorkQualifications2,
                :WorkQualifications3, :WorkQualifications4, :WorkQualifications5, :WhetherPromoted,
                :PromotedSpeed, :ProjectHours, :ProjectTotal, :CurrentProjectRole, :ProportionOfSpecialProject,
                :WorkPlace, :TrainingHoursA, :TrainingHoursB, :TrainingHoursC, :TotalProduction, :NumberOfHonors,
                :CommutingCosts, :Leave3A, :Leave3B, :LeaveYearA, :LeaveYearB, :BusinessTripA, :BusinessTripB,
                :BusinessTripConcentration, :AnnualPerformanceGradeA, :AnnualPerformanceGradeB, :AnnualPerformanceGradeC,
                :AgeLevel, :MaritalStatus, :Dependents, :SeniorityA, :SeniorityB, :SeniorityC, :AverageYear,
                :Education, :School, :Department
            )''', data)
            conn.commit()
            self.success.setText("已新增成功")
            self.clear_text_fields()
            
        except sqlite3.IntegrityError:
            self.success.setText("因有欄目未被填寫或員工在職狀態、編號異常\n，故加入資料庫失敗，請重新填寫")
        finally:
            conn.close()


    def update_employee(self):
        data = self.get_employee_data()
        PerNo = data.pop("PerNo")
        
        if not PerNo:
            self.success.setText("請輸入員工編號以進行更新")
            return
        
        set_clause = ", ".join([f"{key} = :{key}" for key in data.keys() if data[key]])
        if not set_clause:
            self.success.setText("沒有要更新的資料")
            return
        
        query = f"UPDATE employees SET {set_clause} WHERE PerNo = :PerNo"
        data["PerNo"] = PerNo
        
        conn = sqlite3.connect('employee_management.db')
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        
        self.success.setText("已更新成功")

    def delete_employee(self):
        PerNo = self.PerNo.text()  # 從UI得到PerNo
        
        if not PerNo:  # 檢查PerNo是否為填寫
            self.success.setText("請輸入PerNo以進行刪除")  # 如果為空，提示輸入PerNo
            return  # 退出方法，不继续执行
        
        conn = sqlite3.connect('employee_management.db')  # 連接資料庫
        cursor = conn.cursor()  
        
        cursor.execute("SELECT * FROM employees WHERE PerNo = ?", (PerNo,))  # 用PerNo查詢員工
        employee = cursor.fetchone()  # 獲得查詢到的資料
        
        if not employee:  # 沒找到員工的情況
            self.success.setText("找不到該員工")  
            conn.close() 
            return  
        
        data = self.get_employee_data()  # 获取用户输入的员工数据，返回一个字典
        column_names = [desc[0] for desc in cursor.description]  
        
        
        # 核對有輸入的部分，是否資料相同
        for key, value in data.items():
            db_value = employee[column_names.index(key)]  # 從資料庫獲得資料
            if value and str(value) != str(db_value):  # 比較時轉換為相同型態的資料
                self.success.setText("輸入資料和資料庫內資料不符，刪除失敗")
                conn.close()  
                return 
    
        cursor.execute("DELETE FROM employees WHERE PerNo = ?", (PerNo,))  # 如果相同就刪除
        conn.commit()  
        self.success.setText("已刪除成功") 
        
        conn.close()  




    def go_to_previous_page(self):
        from nextpage import NextPageWindow
        self.next_page = NextPageWindow()
        self.next_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManageEmployeeInformationWindow()
    window.show()
    sys.exit(app.exec_())
