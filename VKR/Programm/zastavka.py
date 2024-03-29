import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QProgressBar, QVBoxLayout, QApplication
from autorization import Ui_Form_utorization
from PyQt5 import QtCore, QtGui, QtWidgets

class Thread(QThread):
    _signal = pyqtSignal(int)
    def __init__(self):
        super(Thread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(100):
            time.sleep(0.01)
            self._signal.emit(i)

 
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.setWindowTitle('Ychpo')
        self.btn = QPushButton('Проверить обновления')
        self.btn.clicked.connect(self.btnFunc)
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)
        self.resize(300, 100)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.pbar)
        self.vbox.addWidget(self.btn)
        self.setLayout(self.vbox)
        self.show()
        
    def btnFunc(self):
        self.thread = Thread()
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()
        self.btn.setEnabled(False)

    def signal_accept(self, msg):
        self.pbar.setValue(int(msg))
        if self.pbar.value() == 99:
            self.pbar.setValue(0)

            
            app = QtWidgets.QApplication(sys.argv)
            Form_utorization = QtWidgets.QMainWindow()
            ui = Ui_Form_utorization()
            ui.setupUi(Form_utorization)
            Form_utorization.show()
            sys.exit(app.exec_())

            pass
            self.btn.setEnabled(True)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())