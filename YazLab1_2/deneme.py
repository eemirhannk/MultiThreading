import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from urunEkle import *

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

def senaryo1():

    




ui.btnEkle.clicked.connect(senaryo1)

sys.exit(uygulama.exec_())


