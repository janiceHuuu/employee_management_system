import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
from login_ui import Ui_MainWindow as Ui_LoginWindow
from nextpage import NextPageWindow
from PyQt5.QtGui import QIcon

class LoginWindow(QMainWindow, Ui_LoginWindow):
    login_success = pyqtSignal()  # 定義一個信號
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.check_login)

    def check_login(self):
        if self.usernameLineEdit.text() == "user" and self.passwordLineEdit.text() == "pass":
            self.messageLabel.setText("Sign in successful!")
            self.login_success.emit()  # 發射信號
            self.close()
            #self.open_next_page()
    
        else:
            self.messageLabel.setText("    帳號或密碼錯誤，請重新輸入")
            
    #def open_next_page(self):
        #self.next_page = NextPageWindow()
        #self.next_page.show()
        #self.close()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.setWindowIcon(QIcon('icon/azvtu-m979f-001.ico'))
    window.show()
    sys.exit(app.exec_())
