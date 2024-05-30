import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from drawing_answer_ui import Ui_MainWindow as Ui_DrawingAnswerWindow


class DrawingAnswerWindow(QMainWindow, Ui_DrawingAnswerWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.previous_page.clicked.connect(self.go_to_previous_page)

    def go_to_previous_page(self):
        from visual_drawing import VisualDrawingWindow
        self.visual_drawing_page = VisualDrawingWindow()
        self.visual_drawing_page.show()
        self.close()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawingAnswerWindow()
    window.show()
    sys.exit(app.exec_())
