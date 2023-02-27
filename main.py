import cv2
import numpy as np

# Load fisheye photo
img = cv2.imread('fisheye_photo.jpg')

# Define camera calibration parameters
K = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]], dtype=np.float32)
D = np.array([0.01, 0.01, 0, 0], dtype=np.float32)

# Undistort fisheye image to cylindrical image
img_cyl = cv2.fisheye.undistortImage(img, K, D, Knew=K)

# Convert cylindrical image to perspective image
height, width = img_cyl.shape[:2]
fov = 180
f = 0.5 * width / np.tan(fov * np.pi / 360)
K_persp = np.array([[f, 0, width/2], [0, f, height/2], [0, 0, 1]])
R = np.eye(3)
T = np.array([0, 0, f])
# Define the perspective transformation matrix
P = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32)
# Apply the perspective transformation
img_persp = cv2.warpPerspective(img_cyl, P, (width, height), flags=cv2.INTER_LINEAR)

# Create distance grid
grid_size = 10  # in meters
grid_step = 100  # in pixels
for i in range(grid_step, height, grid_step):
    cv2.putText(img_persp, f'{i//grid_step*grid_size}m', (10, i), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
for j in range(grid_step, width, grid_step):
    cv2.putText(img_persp, f'{j//grid_step*grid_size}m', (j, height-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Overlay distance grid onto perspective image
alpha = 0.5
overlay = img_persp.copy()
cv2.rectangle(overlay, (0, 0), (width, height), (0, 0, 255), -1)
img_persp = cv2.addWeighted(overlay, alpha, img_persp, 1 - alpha, 0)

# Display or save resulting image
cv2.imshow('Distance Grid', img_persp)
cv2.waitKey(0)
cv2.destroyAllWindows()
