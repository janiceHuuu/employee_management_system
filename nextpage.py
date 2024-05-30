import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from nextpage_ui import Ui_MainWindow as Ui_NextPageWindow
from manage_employee_information import ManageEmployeeInformationWindow
from employee_turnover_forecast import EmployeeTurnoverForecastWindow
from visual_drawing import VisualDrawingWindow

class NextPageWindow(QMainWindow, Ui_NextPageWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.manage_employee_information.clicked.connect(self.open_manage_employee_information)
        self.employee_turnover_forecast.clicked.connect(self.open_employee_turnover_forecast)
        self.visual_drawing.clicked.connect(self.open_visual_drawing)

    def open_manage_employee_information(self):
        self.manage_employee_info_page = ManageEmployeeInformationWindow()
        self.manage_employee_info_page.show()
        self.close()

    def open_employee_turnover_forecast(self):
        self.employee_turnover_forecast_page = EmployeeTurnoverForecastWindow()
        self.employee_turnover_forecast_page.show()
        self.close()

    def open_visual_drawing(self):
        self.visual_drawing_page = VisualDrawingWindow()
        self.visual_drawing_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NextPageWindow()
    window.show()
    sys.exit(app.exec_())
