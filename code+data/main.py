import sys
from PyQt5.QtWidgets import QApplication
from login import LoginWindow
from nextpage import NextPageWindow
from manage_employee_information import ManageEmployeeInformationWindow
from employee_turnover_forecast import EmployeeTurnoverForecastWindow
#from search_employee_information import SearchEmployeeInformationWindow
from visual_drawing import VisualDrawingWindow
#from search_answer import SearchAnswerWindow
from drawing_answer import DrawingAnswerWindow
from PyQt5.QtGui import QIcon


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 創建並顯示登錄界面
    login_window = LoginWindow()
    login_window.setWindowIcon(QIcon('icon/azvtu-m979f-001.ico'))
    login_window.show()


    # 創建其他窗口實例，但初始時不顯示
    next_page_window = NextPageWindow()
    next_page_window.setWindowIcon(QIcon('icon/azvtu-m979f-001.ico'))
    manage_employee_window = ManageEmployeeInformationWindow()
    manage_employee_window.setWindowIcon(QIcon('icon/azvtu-m979f-001.ico'))
    employee_turnover_forecast_window = EmployeeTurnoverForecastWindow()
    employee_turnover_forecast_window.setWindowIcon(QIcon('icon/azvtu-m979f-001.ico'))
    #search_employee_information_window = SearchEmployeeInformationWindow()
    visual_drawing_window = VisualDrawingWindow()
    visual_drawing_window.setWindowIcon(QIcon('icon/azvtu-m979f-001.ico'))
    #search_answer_window = SearchAnswerWindow([])
    drawing_answer_window = DrawingAnswerWindow([])
    drawing_answer_window.setWindowIcon(QIcon('icon/azvtu-m979f-001.ico'))
    
    # 登錄窗口中的信號連接到主界面和其他界面的切換功能
    #print(type(login_window.login_success))
    login_window.login_success.connect(lambda: next_page_window.show())
    #login_window.login_success.clicked.connect(next_page_window.show)

    # nextpage 界面中的信號連接到其他界面的切換功能
    #print(type( next_page_window.manage_employee_information))
   
    next_page_window.manage_employee_information.clicked.connect(lambda: manage_employee_window.show)
    next_page_window.employee_turnover_forecast.clicked.connect(lambda: employee_turnover_forecast_window.show)
    next_page_window.visual_drawing.clicked.connect(lambda: visual_drawing_window.show)
    #next_page_window.search_employee_information.clicked.connect(lambda: search_employee_information_window.show)

    # search_employee_information_window 界面中的信號連接到 nextpage 界面的切換功能
    #search_employee_information_window.previous_page.clicked.connect(lambda: next_page_window.show)
    
    # manage_employee_information 界面中的信號連接到 nextpage 界面的切換功能
    manage_employee_window.previous_page.clicked.connect(lambda: next_page_window.show)
    
    # manage_employee_information 界面中的信號連接到 nextpage 界面的切換功能
    visual_drawing_window.previous_page.clicked.connect(lambda: next_page_window.show)
    
    # search_employee_information 界面中的信號連接到 search_answer 界面的切換功能
    #search_employee_information_window.search.clicked.connect(lambda: search_answer_window.show)

    # search_answer 界面中的信號連接到 search_employee_information 界面的切換功能
    #search_answer_window.previous_page.clicked.connect(lambda: search_employee_information_window.show)
    
    # visual_drawing 界面中的信號連接到 drawing_answer 界面的切換功能
    visual_drawing_window.drawing.clicked.connect(lambda: drawing_answer_window.show)

    # drawing_answer 界面中的信號連接到 visual_drawing 界面的切換功能
    drawing_answer_window.previous_page.clicked.connect(lambda: visual_drawing_window.show)

    sys.exit(app.exec_())
    
    