import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QCheckBox, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
from visual_drawing_ui import Ui_MainWindow as Ui_VisualDrawingWindow

class DrawingAnswerWindow(QMainWindow):
    def __init__(self, selected_field):
        super().__init__()
        self.selected_field = selected_field
        self.setWindowTitle("Drawing Answer")
        self.initUI()
        self.plot_relationship()

    def initUI(self):
        self.resize(1000, 800)  # Set the window size to be larger
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)

        # Add the "Previous Page" button
        self.top_layout = QHBoxLayout()
        self.previous_button = QPushButton("上一頁", self)
        self.previous_button.clicked.connect(self.go_to_previous_page)
        self.top_layout.addWidget(self.previous_button)
        self.top_layout.addStretch()  # Push the button to the left

        self.main_layout.addLayout(self.top_layout)

        # Add the canvas for the plot
        self.canvas = FigureCanvas(plt.Figure())
        self.main_layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111)

    def plot_relationship(self):
        df = pd.read_csv('train.csv')

        if self.selected_field not in df.columns:
            QMessageBox.warning(self, "Error", "選擇的選項不存在於資料集中")
            return

        selected_columns = ['PerStatus', self.selected_field]
        df_selected = df[selected_columns]
        df_selected = df_selected.dropna()

        if self.selected_field == 'sex':
            status_sex_count = df_selected.groupby(['sex', 'PerStatus']).size().unstack(fill_value=0)
            status_sex_percent = status_sex_count.div(status_sex_count.sum(axis=1), axis=0) * 100
            status_sex_percent.plot(kind='bar', stacked=True, ax=self.ax)
            self.ax.set_xticks([0, 1])
            self.ax.set_xticklabels(['Female', 'Male'])

        elif self.selected_field == 'year':
            df_selected = df_selected[df_selected['year'].isin([2014, 2015, 2016, 2017])]
            status_year_count = df_selected.groupby(['year', 'PerStatus']).size().unstack(fill_value=0)
            status_year_percent = status_year_count.div(status_year_count.sum(axis=1), axis=0) * 100
            status_year_percent.plot(kind='bar', stacked=True, ax=self.ax)

        elif self.selected_field == 'CommutingCosts':
            df_selected['CommutingCosts_bin'] = pd.cut(df_selected['CommutingCosts'], bins=5)
            group_col = 'CommutingCosts_bin'
            status_commutingcosts_count = df_selected.groupby([group_col, 'PerStatus']).size().unstack(fill_value=0)
            status_commutingcosts_percent = status_commutingcosts_count.div(status_commutingcosts_count.sum(axis=1), axis=0) * 100
            status_commutingcosts_percent.plot(kind='bar', stacked=True, ax=self.ax)

        elif self.selected_field in ['Job_classification', 'Grade', 'FactoryCode', 'ManageLevel', 'WorkQualifications1',
                                     'WorkQualifications2', 'WorkQualifications3', 'WorkQualifications4', 'WorkQualifications5',
                                     'CurrentProjectRole', 'WorkPlace', 'Education', 'School', 'Department', 'Dependents', 
                                     'BelongingDepartment', 'MaritalStatus', 'AgeLevel']:
            status_count = df_selected.groupby([self.selected_field, 'PerStatus']).size().unstack(fill_value=0)
            status_percent = status_count.div(status_count.sum(axis=1), axis=0) * 100
            status_percent.plot(kind='bar', stacked=True, ax=self.ax)

        elif self.selected_field in ['ProjectHours', 'ProjectTotal', 'ProportionOfSpecialProject', 'TrainingHoursA',
                                     'TrainingHoursB', 'TotalProduction', 'NumberOfHonors', 'PromotedSpeed', 'Leave3A',
                                     'LeaveYearA', 'Leave3B', 'LeaveYearB', 'BusinessTripA', 'BusinessTripB', 
                                     'BusinessTripConcentration', 'AnnualPerformanceGradeA', 'AnnualPerformanceGradeB', 
                                     'AnnualPerformanceGradeC', 'SeniorityA', 'SeniorityB', 'SeniorityC']:
            df_selected[f'{self.selected_field}_bin'] = pd.cut(df_selected[self.selected_field], bins=5)
            group_col = f'{self.selected_field}_bin'
            status_count = df_selected.groupby([group_col, 'PerStatus']).size().unstack(fill_value=0)
            status_percent = status_count.div(status_count.sum(axis=1), axis=0) * 100
            status_percent.plot(kind='bar', stacked=True, ax=self.ax)

        elif self.selected_field == 'WhetherPromoted':
            status_count = df_selected.groupby(['WhetherPromoted', 'PerStatus']).size().unstack(fill_value=0)
            status_percent = status_count.div(status_count.sum(axis=1), axis=0) * 100
            status_percent.plot(kind='bar', stacked=True, ax=self.ax)

        else:
            QMessageBox.warning(self, "Error", f"Unexpected field: {self.selected_field}")
            return

        self.ax.set_title(f'The relationship between resignation and {self.selected_field}')
        self.ax.set_xlabel(self.selected_field)
        self.ax.set_ylabel('Percentage of people (%)')
        self.ax.legend(title='whether to resign', labels=['staying', 'having resigned'])
        self.ax.grid(axis='y')

        self.canvas.draw()

    def go_to_previous_page(self):
        from nextpage import NextPageWindow
        self.next_page = NextPageWindow()
        self.next_page.show()
        self.close()

class VisualDrawingWindow(QMainWindow, Ui_VisualDrawingWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.previous_page.clicked.connect(self.go_to_previous_page)
        self.drawing.clicked.connect(self.create_drawing)

        for checkbox in self.findChildren(QCheckBox):
            checkbox.stateChanged.connect(self.handle_checkbox_state_change)

        self.last_checked_checkbox = None

    def handle_checkbox_state_change(self, state):
        if state == Qt.Checked:
            sender_checkbox = self.sender()
            if self.last_checked_checkbox and self.last_checked_checkbox != sender_checkbox:
                self.last_checked_checkbox.setChecked(False)
            self.last_checked_checkbox = sender_checkbox

    def create_drawing(self):
        selected_checkboxes = [
            checkbox for checkbox in self.findChildren(QCheckBox) if checkbox.isChecked()
        ]

        if len(selected_checkboxes) != 1:
            QMessageBox.warning(self, "Error", "請選擇且只能選擇一個選項")
            return

        selected_field = selected_checkboxes[0].objectName()  # Get the objectName of the selected checkbox
        print("Selected Field in create_drawing:", selected_field)  # Check the value of selected_field

        self.drawing_answer_page = DrawingAnswerWindow(selected_field)
        self.drawing_answer_page.show()
        self.close()

    def go_to_previous_page(self):
        from nextpage import NextPageWindow
        self.next_page = NextPageWindow()
        self.next_page.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VisualDrawingWindow()
    window.show()
    sys.exit(app.exec_())
