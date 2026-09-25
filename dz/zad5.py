import cv2
import numpy as np

h, w = 400, 600
channels = 3

image = np.zeros((h, w, channels), dtype=np.uint8)

for y in range(h):
    for x in range(w):
        image[y, x] = [x % 255, y % 255, (x + y) % 255]

cv2.imwrite("grad.png", image)
