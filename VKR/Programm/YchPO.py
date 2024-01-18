from main import Ui_MainWindow
from autorization import Ui_Form_utorization
from PyQt5 import QtCore, QtGui, QtWidgets
from allwidjets import *


class YchPo():
    def show(self):
        global Form_utorization, Form_main, app
        

        ui = Ui_Form_utorization()

        ui.setupUi(Form_utorization)
        Form_utorization.show()

        ui1 = Ui_MainWindow()
        ui1.setupUi(Form_main)

        sys.exit(app.exec_())


ychpo = YchPo()
ychpo.show()