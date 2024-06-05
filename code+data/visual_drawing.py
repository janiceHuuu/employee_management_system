import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QCheckBox
from PyQt5.QtCore import Qt
from visual_drawing_ui import Ui_MainWindow as Ui_VisualDrawingWindow
from drawing_answer import DrawingAnswerWindow  

class VisualDrawingWindow(QMainWindow, Ui_VisualDrawingWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.previous_page.clicked.connect(self.go_to_previous_page)
        self.drawing.clicked.connect(self.create_drawing)

        # Connect checkbox state changed signal to handler
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
        # Pass the selected_field to DrawingAnswerWindow
        self.drawing_answer_page = DrawingAnswerWindow(selected_field)  # Pass selected_field argument
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
