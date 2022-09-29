import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

import GUI

#Clase de la interfaz
class app_VRU(QtWidgets.QMainWindow):
    def __init__(self):
        #Cargando interfaz
        super().__init__()
        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self)

#Inicio de la interfaz
if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = app_VRU()
    mainWindow.show()
    sys.exit(app.exec_())
