import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_ui import Ui_MainWindow as Ui_LoginWindow
from nextpage import NextPageWindow  

class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.check_login)

    def check_login(self):
        if self.usernameLineEdit.text() == "user" and self.passwordLineEdit.text() == "pass":
            self.messageLabel.setText("Sign in successful!")
            self.open_next_page()
            #self.accepted.emit()  # Emit a custom signal indicating successful login
        else:
            self.messageLabel.setText("Incorrect username or password.\nPlease try again.")
            
    def open_next_page(self):
        self.next_page = NextPageWindow()
        self.close()
        self.next_page.show()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
