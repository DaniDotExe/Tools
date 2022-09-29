import cv2                                # state of the art computer vision algorithms library
import numpy as np                        # fundamental package for scientific computing
import matplotlib.pyplot as plt           # 2D plotting library producing publication quality figures
import pyrealsense2 as rs  
#Importar archivos
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage, QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import cv2
import pyrealsense2 as rs
import numpy as np
from cam_folder import *
import os

#only Cam


# Setup:
pipe = rs.pipeline()
cfg = rs.config()
cfg.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

pipe.start(cfg)

#Clase de la interfaz
class MainWindow(QWidget):

    #valor inicial para guardar la imagen (en realidad empezaara en Imagen_1)
    nombre='Imagen_0.jpg'
    carpeta='Toma_1'
    view_imagen1 = 0

    pipe = rs.pipeline()
    cfg = rs.config()
    cfg.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

    pipe.start(cfg)

    #constructor
    def __init__(self):
        super().__init__()
        
        #interfaz
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Capture")
        self.setWindowIcon(QIcon("logo.png"))


try: 
  while True:
    # Store next frameset for later processing:
    frameset = pipe.wait_for_frames()
    color_frame = frameset.get_color_frame()
    depth_frame = frameset.get_depth_frame()
 

    #Componente de color
    color = np.asanyarray(color_frame.get_data())

    cv2.imshow('Cam',color)
    cv2.waitKey(1) 


finally:
  # Cleanup:
  pipe.stop()
  print("Frames Captured")
