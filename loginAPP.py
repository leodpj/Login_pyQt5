from PyQt5 import QtWidgets, QtSql
from loginUi import Ui_Form
import sys

class myApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(myApp, self).__init__()
        self.setupUi(self)
        self.openDB()
        self.pushButton.clicked.connect(self.checkUser)

    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.sqlite")
        if not self.db.open():
            print("Error")
        self.query = QtSql.QSqlQuery()

    def checkUser(self):
        username1 = self.lineEdit.text()
        password1 = self.lineEdit_2.text()
        print(username1, password1)
        self.query.exec_("select * from userdata where username = '%s' and password = '%s';"%(username1, password1))
        self.query.first()
        if self.query.value("username") != None and self.query.value("password") != None:
            print("Login successfull!")
        else:
            print("login failed")

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = myApp()
        Form.show()
        sys.exit(app.exec_())