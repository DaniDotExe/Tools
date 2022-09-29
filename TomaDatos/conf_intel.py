import cv2                                # state of the art computer vision algorithms library
import numpy as np                        # fundamental package for scientific computing
import matplotlib.pyplot as plt           # 2D plotting library producing publication quality figures
import pyrealsense2 as rs  

#only Cam
# Setup:
pipe = rs.pipeline()
cfg = rs.config()
cfg.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

pipe.start(cfg)

try: 
  while True:
    # Store next frameset for later processing:
    frameset = pipe.wait_for_frames()
    color_frame = frameset.get_color_frame()

    #Componente de color
    color = np.asanyarray(color_frame.get_data())

    cv2.imshow('Cam',color)
    cv2.waitKey(1) 


finally:
  # Cleanup:
  pipe.stop()
  print("Frames Captured")
