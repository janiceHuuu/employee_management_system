import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QScrollArea, QPushButton, QApplication
from forecast_answer_ui import Ui_MainWindow as Ui_ForecastAnswerWindow


class Ui_ForecastAnswerWindow(QMainWindow, Ui_ForecastAnswerWindow):
    def __init__(self, results):
        super().__init__()
        self.results = results
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Forecast Answer")
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        
        self.scrollAreaWidgetContents.setLayout(QVBoxLayout())
        self.addLabels()
        
        self.previous_page = QPushButton("Previous Page", self.centralwidget)
        self.verticalLayout.addWidget(self.previous_page)
        self.previous_page.clicked.connect(self.go_to_previous_page)

    def addLabels(self):
        layout = self.scrollAreaWidgetContents.layout()
        for result in self.results:
            for key, value in result.items():
                if key != "PerStatus":
                    label = QLabel(f"{key}: {value}")
                    layout.addWidget(label)
                    
    def go_to_previous_page(self):
        from employee_turnover_forecast import EmployeeTurnoverForecastWindow
        self.employee_turnover_forecast = EmployeeTurnoverForecastWindow()
        self.employee_turnover_forecast.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    results = [{"key1": "value1"}, {"key2": "value2"}]  # 從資料庫中獲得的結果
    window = Ui_ForecastAnswerWindow(results)
    window.show()
    sys.exit(app.exec_())



