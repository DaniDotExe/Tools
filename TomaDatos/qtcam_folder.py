#Importar archivos
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import cv2
from cam_folder import *
import os

#Clase de la interfaz
class MainWindow(QWidget):

    #valor inicial para guardar la imagen (en realidad empezaara en Imagen_1)
    nombre='Imagen_0.jpg'
    carpeta='Toma_1'
    view_imagen1 = 0

    #constructor
    def __init__(self):
        super().__init__()
        
        #interfaz
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Capture")
        self.setWindowIcon(QIcon("logo.png"))

        #crea timer
        self.timer = QTimer()

        #cuando se inicie el timer se ejecutara esto cada ciclo del timer
        self.timer.timeout.connect(self.ejecutar_nombrar)
        self.timer.timeout.connect(self.viewCam)

        #enlace con boton de start/stop
        self.ui.START.clicked.connect(self.controlTimer)

    #creada para llamar a la funcion nombrar por que la linea 29 no permite guardar el retorno del metodo nombrar
    def ejecutar_nombrar(self):
        nombrando = self.nombrar(self.nombre)
        self.archivofinal = f'./{self.carpeta}/Imagen_{nombrando}.jpg'
        self.nombre = f'Imagen_{nombrando}.jpg'
        self.view_imagen1 = nombrando
        

        
    #mostrar y guardar datos de la camara   
    def viewCam(self):
        #leer imagen en formato BGR
        ret, image = self.cap.read() 
        #conversion a RGB
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #obtener datos de imagen
        height, width, channel = new_image.shape
        step= channel*width
        #crear QImage para imagen
        qImg=QImage(new_image.data,width,height,step,QImage.Format_RGB888)
        #mostrar en el label
        self.ui.LIVE.setPixmap(QPixmap.fromImage(qImg))
        #guardar imagen
        cv2.imwrite(self.archivofinal,new_image)
        
        self.ui.VIEW_IMAGEN.setText(f'{self.view_imagen1}')
        self.ui.VIEW_TOMA.setText(f'{self.carpeta}')

    #Start/Stop timer es decir inicia funciones del comando 29 y 30 (ejecutar_nomrar) y (viewCam) 
    def controlTimer(self):
        #Si el timer esta detenido
        if not self.timer.isActive():
            #crea video capture
            self.cap = cv2.VideoCapture(0)
            #1920x1080
            #estabecer resolucion
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
            #obtener resolucion
            width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print(width,height)
            # estabecer FPS
            self.cap.set(cv2.CAP_PROP_FPS, 30)
            # obtener fps
            fps = self.cap.get(cv2.CAP_PROP_FPS)
            print(fps)
            #self.cap.set(cv2.CAP_PROP_AUTOFOCUS,0)
            #self.cap.set(cv2.CAP_PROP_FOCUS, 0)
            try:
                os.mkdir(f'./{self.carpeta}')
            except:
                pass
            #Start timer 
            self.timer.start(5) #ACA SE COLOCA EL TIEMPO EN MILISEGUNDOS PARA GUARDAR LOS ARCHIVOS!!!!!!!!!!!!!!!!!!!!!!!!! 
            #Cargar en el boton de start
            self.ui.START.setText("Stop")

        #si el timer esta iniciado
        else:
            #Stop timer
            self.timer.stop()
            #release video capture
            self.cap.release()
            #cargar texto del control start
            self.ui.START.setText("Start")
            nombrando_carpeta = self.nombrar(self.carpeta)
            self.carpeta = f'Toma_{nombrando_carpeta}'
            print(nombrando_carpeta)

    #cambia el nombre de la imagen
    def nombrar(self,name):
        #obtiene numero actual
        filtro = list(filter(str.isdigit, name))
        numero = int("" .join(filtro))
        #aumenta el numero actual
        new_name = f'{numero+1}'
        return new_name
        


if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


