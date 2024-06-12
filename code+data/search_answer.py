import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from search_answer_ui import Ui_MainWindow as Ui_SearchAnswerWindow
import sqlite3

class SearchAnswerWindow(QMainWindow, Ui_SearchAnswerWindow):
    def __init__(self, results):
        super().__init__()
        self.setupUi(self)
        self.results = results
        self.display_results()
        self.previous_page.clicked.connect(self.go_to_previous_page)

    def display_results(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
    
        main_layout = QVBoxLayout(central_widget)
    
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.previous_page, alignment=Qt.AlignLeft | Qt.AlignTop)
        main_layout.addLayout(button_layout)
    
        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    
        scroll_widget = QWidget()
        scroll_layout = QGridLayout(scroll_widget)
    
        # 將 UI 中的 QLabel 值添加到第一列
        for col in range(1, 48):
            label_name = f'label_{col}'
            label_value = getattr(self, label_name).text()
            header_label = QLabel(label_value)
            scroll_layout.addWidget(header_label, 0, col - 1)
    
        for row, result in enumerate(self.results, start=1):
            per_status = result[3]  # PerStatus 位於資料中的第四個位置
            # 檢查 PerStatus 是否為 0，如果是則跳過
            #if per_status == 0:
                #continue
            for col, value in enumerate(result):
                # 如果不是 PerStatus 所在列，則添加該值
                if col != 3:
                    data_label = QLabel(str(value))
                    # 修正欄位位置的計算，跳過 PerStatus 的索引
                    if col < 3:
                        scroll_layout.addWidget(data_label, row, col)
                    else:
                        scroll_layout.addWidget(data_label, row, col - 1)
    
        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)
    
        main_layout.addWidget(scroll_area)

    def go_to_previous_page(self):
        from search_employee_information import SearchEmployeeInformationWindow
        self.search_employee_information_page = SearchEmployeeInformationWindow()
        self.search_employee_information_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchAnswerWindow([])
    window.show()
    sys.exit(app.exec_())
