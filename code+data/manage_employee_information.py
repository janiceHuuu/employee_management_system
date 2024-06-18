import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
import sqlite3
from manage_employee_information_ui import Ui_MainWindow as Ui_ManageEmployeeInformationWindow
from PyQt5.QtGui import QIcon

class ManageEmployeeInformationWindow(QMainWindow, Ui_ManageEmployeeInformationWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_employee_information.clicked.connect(self.add_employee)
        self.update_employee_information.clicked.connect(self.update_employee)
        self.delet_employee_information.clicked.connect(self.delete_employee)
        self.previous_page.clicked.connect(self.go_to_previous_page)
        self.conn = None  # 資料庫連接物件初始化
    
    def connect_database(self):
        self.conn = sqlite3.connect('employee_management.db', timeout=100)
        cursor = self.conn.cursor()
        cursor.execute('PRAGMA journal_mode = WAL;')
        self.conn.commit()
    
    def disconnect_database(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f"資料庫關閉時出錯: {str(e)}")


    def add_employee(self):
        data = self.get_employee_data()
        
        if any(value == "" for value in data.values()):
            self.success.setText("有欄目未被填寫或編號異常，請重新填寫")
            return
        
        try:
            self.connect_database()
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute('SELECT PerNo FROM PredictionEmployee WHERE PerNo = ?', (data['PerNo'],))
                if cursor.fetchone() is not None:
                    self.success.setText("員工編號已存在，請重新填寫")
                    return
                
                cursor.execute('''
                    INSERT INTO PredictionEmployee VALUES (
                        :yyyy, :PerNo, :最新離職預測, :sex, :工作分類, :職等, :廠區代碼,
                        :管理層級, :歸屬部門, :工作資歷1, :工作資歷2, :工作資歷3, :工作資歷4, :工作資歷5,
                        :是否升遷, :升遷速度, :專案時數, :專案總數, :當前專案角色, :特殊專案佔比, :工作地點, 
                        :訓練時數A, :訓練時數B, :訓練時數C, :生產總額, :榮譽數, :通勤成本, :近三月請假數A, 
                        :近三月請假數B, :近一年請假數A, :近一年請假數B, :出差數A, :出差數B, :出差集中度, 
                        :年度績效等級A, :年度績效等級B, :年度績效等級C, :年齡層級, :婚姻狀況, :眷屬量, 
                        :年資層級A, :年資層級B, :年資層級C, :任職前工作平均年數, :最高學歷, :畢業學校類別, 
                        :畢業科系類別
                    )
                ''', data)
                self.success.setText("已新增成功")
                self.clear_text_fields()
                
        except sqlite3.Error as e:
            self.success.setText(f"資料庫錯誤: {str(e)}")
        finally:
            self.disconnect_database()
    
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
        
        query = f"UPDATE PredictionEmployee SET {set_clause} WHERE PerNo = :PerNo"
        data["PerNo"] = PerNo
        
        try:
            self.connect_database()
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute(query, data)
                self.success.setText("已更新成功")
                self.clear_text_fields()
                
        except sqlite3.Error as e:
            self.success.setText(f"資料庫錯誤: {str(e)}")
        finally:
            self.disconnect_database()
    
    def delete_employee(self):
        PerNo = self.PerNo.text()
        
        if not PerNo:
            self.success.setText("請輸入員工編號以進行刪除")
            return
        
        try:
            self.connect_database()
            with self.conn:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM PredictionEmployee WHERE PerNo = ?", (PerNo,))
                employee = cursor.fetchone()
                
                if not employee:
                    self.success.setText("找不到該員工")
                    return
                data = self.get_employee_data()  # 獲取用戶輸入的員工數據
                column_names = [desc[0] for desc in cursor.description]
                
                # 核對用戶輸入的部分，確認是否與資料庫中的數據一致
                for key, value in data.items():
                    db_value = employee[column_names.index(key)]
                    if value and str(value) != str(db_value):
                        self.success.setText("輸入資料和資料庫內資料不符，刪除失敗")
                        return
                
                cursor.execute("DELETE FROM PredictionEmployee WHERE PerNo = ?", (PerNo,))
                self.success.setText("已刪除成功")
                self.clear_text_fields()
                
        except sqlite3.Error as e:
            self.success.setText(f"資料庫錯誤: {str(e)}")
        finally:
            self.disconnect_database()

    def get_employee_data(self):
        return {
            "yyyy": self.Year.text(),
            "PerNo": self.PerNo.text(),
            '最新離職預測': 3,
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
    
    def clear_text_fields(self):
        for widget in self.findChildren(QLineEdit):
            widget.clear()
    
    def go_to_previous_page(self):
        from nextpage import NextPageWindow
        self.next_page = NextPageWindow()
        self.next_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManageEmployeeInformationWindow()
    window.setWindowIcon(QIcon('icon/azvtu-m979f-001.ico'))
    window.show()
    sys.exit(app.exec_())
