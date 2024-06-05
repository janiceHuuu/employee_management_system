import sys
from PyQt5.QtWidgets import QApplication
from ui.login import LoginWindow
from ui.nextpage import NextPageWindow
from ui.manage_employee_information import ManageEmployeeInformationWindow
from ui.employee_turnover_forecast import EmployeeTurnoverForecastWindow
from ui.visual_drawing import VisualDrawingWindow
from ui.forecast_answer import ForecastAnswerWindow
from ui.drawing_answer import DrawingAnswerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建并显示登录界面
    login_window = LoginWindow()
    login_window.show()

    # 创建其他窗口实例，但初始时不显示
    next_page_window = NextPageWindow()
    manage_employee_window = ManageEmployeeInformationWindow()
    employee_turnover_forecast_window = EmployeeTurnoverForecastWindow()
    visual_drawing_window = VisualDrawingWindow()
    forecast_answer_window = ForecastAnswerWindow()
    drawing_answer_window = DrawingAnswerWindow()

    # 登录窗口中的信号连接到主界面和其他界面的切换功能
    login_window.login_success.connect(next_page_window.show)

    # nextpage 界面中的信号连接到其他界面的切换功能
    next_page_window.manage_employee_information.clicked.connect(manage_employee_window.show)
    next_page_window.employee_turnover_forecast.clicked.connect(employee_turnover_forecast_window.show)
    next_page_window.visual_drawing.clicked.connect(visual_drawing_window.show)

    # manage_employee_information 界面中的信号连接到 nextpage 界面的切换功能
    manage_employee_window.go_to_previous_page.connect(next_page_window.show)

    # employee_turnover_forecast 界面中的信号连接到 forecast_answer 界面的切换功能
    employee_turnover_forecast_window.search.clicked.connect(forecast_answer_window.show)

    # forecast_answer 界面中的信号连接到 employee_turnover_forecast 界面的切换功能
    forecast_answer_window.go_to_previous_page.connect(employee_turnover_forecast_window.show)

    # visual_drawing 界面中的信号连接到 drawing_answer 界面的切换功能
    visual_drawing_window.drawing.clicked.connect(drawing_answer_window.show)

    # drawing_answer 界面中的信号连接到 visual_drawing 界面的切换功能
    drawing_answer_window.go_to_previous_page.connect(visual_drawing_window.show)

    sys.exit(app.exec_())
