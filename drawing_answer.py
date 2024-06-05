import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from drawing_answer_ui import Ui_MainWindow as Ui_DrawingAnswerWindow

class DrawingAnswerWindow(QMainWindow, Ui_DrawingAnswerWindow):
    def __init__(self, selected_field):
        super().__init__()
        self.setupUi(self)
        self.selected_field = selected_field  # Save the selected field
        print("Selected Field in init:", self.selected_field)  # Check the value of selected_field
        self.previous_page.clicked.connect(self.go_to_previous_page)
        self.display_selected_field()  # Call the method to display the selected field

    def display_selected_field(self):
        # Display the selected field on the console
        print("Selected Field:", self.selected_field)

    def go_to_previous_page(self):
        from visual_drawing import VisualDrawingWindow
        self.visual_drawing_page = VisualDrawingWindow()
        self.visual_drawing_page.show()
        self.close()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawingAnswerWindow("Default Field")  # Provide a default field for testing
    window.show()
    sys.exit(app.exec_())
