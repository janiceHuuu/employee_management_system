from employee_turnover_forecast_ui import Ui_MainWindow as Ui_EmployeeTurnoverForecastWindow
from emailSending import SendEmail
import sys
import os
import pandas as pd
import numpy as np
import csv
import joblib
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QApplication, QMessageBox, QFileDialog
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class EmployeeTurnoverForecastWindow(QMainWindow, Ui_EmployeeTurnoverForecastWindow):
    def __init__(self):
        super().__init__()
        self.db = None
        self.model = None
        self.setupUi(self)
        self.setFixedSize(850, 650)
        self.connectDatabase()
        self.setLayout()
        self.setTableview()
        self.pushButton.clicked.connect(self.prediction)
        self.actionBack.triggered.connect(self.go_to_previous_page)
        self.pushButton_predict.clicked.connect(self.personal_prediction)
        self.actionExport.triggered.connect(self.dataExport)
        self.emailSender = SendEmail()

    #連接資料庫, 獲取table資料
    def connectDatabase(self):
        if self.db and self.db.isOpen():
            print('關掉db')
            self.db.close()
            QSqlDatabase.removeDatabase("employee_connection")

        self.db = QSqlDatabase.addDatabase("QSQLITE", "employee_connection")
        self.db.setDatabaseName("employee_management.db")

        if not self.db.open():
            print("無法打開資料庫連接")
            sys.exit(1)
        elif self.db.open():
            print('資料庫連接成功')

    #tableview顯示設置
    def setTableview(self):
        query = "SELECT * FROM PredictionEmployee"
        self.model = QSqlQueryModel()
        self.model.setQuery(query, self.db)
        self.tableView.setModel(self.model)
        self.tableView.show()
    
    #layout設置
    def setLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.tableView)
        self.tab.setLayout(layout)

    def fetch_all_data(self):
        while self.model.canFetchMore():
            self.model.fetchMore()

    # 對話視窗
    def messagebox(self, text, title, iconSet, img_icon, button):
        
        message = QMessageBox(self)

        if iconSet == 'info':
            message.setIcon(QMessageBox.Information)
        elif iconSet == 'warn':
            message.setIcon(QMessageBox.Warning)

        if button == 'YesNo':
            message.addButton(QMessageBox.Yes)
            message.addButton(QMessageBox.No)

        message.setWindowTitle(title)
        message.setText(text)
        message.setWindowIcon(QIcon(img_icon))
        result = message.exec_()
        return result

    # 全體離職預測
    def prediction(self):
        
        #讀取資料庫資料，匯出csv檔
        filepath = "file/v2.csv"
        self.csvExport(filepath)
        
        #利用資料庫匯出之csv檔進行離職預測
        df = pd.read_csv(filepath)
        df.fillna(0, inplace = True)
        X = df[['sex', '訓練時數C', '升遷速度', '近一年請假數B', '出差數A',  
                  '年齡層級', '年資層級A', '年資層級B', '任職前工作平均年數', '眷屬量']]
        model_path = 'predictingModel/random_forest_model_v2.joblib'
        loaded_model = joblib.load(model_path)
        predictions = loaded_model.predict(X)
        print(predictions)

        df['最新離職預測'] = predictions
        df.to_csv('file/v2.csv', index = False)


        #更新資料庫資料
        if not self.db.transaction():
            print(f"Failed to start transaction: {self.db.lastError().text()}")
            return

        query2 = QSqlQuery(self.db)
        query2.prepare("UPDATE PredictionEmployee SET 最新離職預測 = :PerStatus WHERE rowid = :rowid")
        for i, prediction in enumerate(predictions):            
            query2.bindValue(":PerStatus", int(prediction))
            query2.bindValue(":rowid", i + 1)
            if not query2.exec_():
                print(f"Failed to update row {i + 1}: {query2.lastError().text()}")
                self.db.rollback()
                return

        if not self.db.commit():
            print(f"Failed to commit transaction: {self.db.lastError().text()}")


        #更新tableview
        self.setTableview()

        #跳出通知視窗，離職預測已經更新完成
        text = "最新離職預測已更新"
        title = '通知'
        iconSet = 'info'
        img_icon = None
        button = None
        r = self.messagebox(text, title, iconSet, img_icon, button)
        if r == QMessageBox.Ok:
            pass

    #個別預測功能
    def personal_prediction(self):
        perNo = self.spinBox.value()
        # print(perNo)

        query = QSqlQuery(self.db)
        query.prepare("SELECT * FROM PredictionEmployee WHERE PerNo = ?")
        query.addBindValue(perNo)

        if query.exec():
            found = False
            while query.next():
                found = True
                x = [query.value(3), query.value(20), query.value(24), query.value(28),
                     query.value(29), query.value(35), query.value(37), query.value(38),
                     query.value(40), query.value(44)]
                df_x = pd.DataFrame({'sex': [x[0]], 
                                     '訓練時數C': [x[1]], 
                                     '升遷速度': [x[2]],
                                     '近一年請假數B': [x[3]], 
                                     '出差數A': [x[4]],
                                     '年齡層級': [x[5]], 
                                     '年資層級A': [x[6]], 
                                     '年資層級B': [x[7]], 
                                     '任職前工作平均年數': [x[8]],
                                     '眷屬量': [x[9]]})
                model_path = 'predictingModel/random_forest_model_v2.joblib'
                model = joblib.load(model_path)
                y_pre = model.predict(df_x)
                
                if y_pre[0] == 0:
                    text = f"編號: {perNo} 員工尚無離職可能性"
                    title = '預測結果'
                    iconSet = 'info'
                    img_icon = None
                    button = None
                    r = self.messagebox(text, title, iconSet, img_icon, button)
                    if r == QMessageBox.Ok:
                        pass
                else:
                    text = f"編號: {perNo} 員工有離職可能\n是否需要發送約談信?"
                    title = '預測結果'
                    iconSet = 'warn'
                    img_icon = None
                    button = 'YesNo'
                    r = self.messagebox(text, title, iconSet, img_icon, button)
                    if r == QMessageBox.Yes:
                        self.emailSender.to = 'f64126147@gs.ncku.edu.tw'
                        self.emailSender.body = self.textEdit.toPlainText()
                        self.emailSender.main()
                        pass
            
            if not found:
                text = "該員工不存在"
                title = '通知'
                iconSet = 'info'
                img_icon = None
                button = 'YesNo'
                r = self.messagebox(text, title, iconSet, img_icon, button)
                if r == QMessageBox.Ok:
                    pass
                
        else:
            print("執行失敗")

    # 選擇路徑匯出csv檔(actionExport)
    def dataExport(self):
        folderPath = QFileDialog.getExistingDirectory(directory = 'file')
        data_path = os.path.join(folderPath, 'Prediction.csv')
        self.csvExport(data_path)
        
    # 匯出csv檔       
    def csvExport(self, datapath):
        query1 = "SELECT * FROM PredictionEmployee"
        self.model.setQuery(query1, self.db)
        self.fetch_all_data()
        
        with open(datapath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
                
            columnHeaders = [self.model.headerData(i, Qt.Horizontal) for i in range(self.model.columnCount())]
            writer.writerow(columnHeaders)
                
            for row in range(self.model.rowCount()):
                rowData = [self.model.data(self.model.index(row, col)) for col in range(self.model.columnCount())]
                writer.writerow(rowData)

    #關閉資料庫連接
    def closeDatabase(self):
        if self.db and self.db.isOpen():
            self.model.clear()
            self.model.deleteLater()
            self.model = None
            self.tableView.setModel(None)
            self.db.close()
            self.db = None
            QSqlDatabase.removeDatabase("employee_connection")
            
            print('關閉資料庫連接')

    #返回選擇頁面
    def go_to_previous_page(self):
        self.closeDatabase()
        from nextpage import NextPageWindow
        self.next_page = NextPageWindow()
        self.next_page.show()
        self.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeTurnoverForecastWindow()
    window.setWindowIcon(QIcon('icon/azvtu-m979f-001.ico'))
    window.show()
    sys.exit(app.exec_())
