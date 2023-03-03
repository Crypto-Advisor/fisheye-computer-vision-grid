import time
import cv2 as cv
import os
import numpy as np
from cv2 import aruco 

# The size of the aruco marker
SQUARE_SIZE = 10.77  # millimeters

# The distance between the aruco markers
SQUARE_SEPERATION = 2.174  # millimeters

# The aruco board size
ARUCO_DIM = (6, 4)

# The calibration data directory path
calib_data_path = "../calib_data"

# The images directory path
image_dir_path = "../images_aruco"

# Get the aruco dictionary of 8x8 markers
aruco_dict = aruco.getPredefinedDictionary( aruco.DICT_6X6_250 )

# create aruco board
board = aruco.GridBoard(ARUCO_DIM, SQUARE_SIZE, SQUARE_SEPERATION, aruco_dict)

img = board.draw((2000, 2000))
cv.show(img)

# files = os.listdir(image_dir_path)
# for file in files:
#     print(file)
#     imagePath = os.path.join(image_dir_path, file)
    
    