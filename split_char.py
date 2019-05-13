from PIL import Image
import numpy as np
from ipdb import set_trace as bp

img = Image.open("3.png")
# temp_img = np.zeros([])
np_img = np.array(img)
# print(np_img.shape)
height, width = np_img.shape[0], np_img.shape[1]
temp_img = np.zeros([height, width, 3], dtype=np.uint8)

temp_img[:, :, 0] = np_img
temp_img[:, :, 1] = np_img
temp_img[:, :, 2] = np_img

for i in range(height):
    for j in range(width):
        if temp_img[i, j, 0] < 195:
            temp_img[i, j, 0] = 0
            temp_img[i, j, 1] = 0
            temp_img[i, j, 2] = 0
        else:
            temp_img[i, j, 0] = 255
            temp_img[i, j, 1] = 255
            temp_img[i, j, 2] = 255


left = 0
for j in range(width):
    flag = False
    for i in range(height):
        if temp_img[i, j, 0] == 0:
            flag = True
    if flag == True:
        left = j
        break

right = width-1
for j in range(width-1, 0, -1):
    flag = False
    for i in range(height):
        if temp_img[i, j, 0] == 0:
            flag = True
    if flag == True:
        right = j
        break

print(left," ",right)
for j in range(left, right+1):
    flag = False
    for i in range(height):
        if temp_img[i, j, 0] == 0:
            flag = True

    if flag == False:
        for i in range(height):
            temp_img[i, j, 0] = 255
            temp_img[i, j, 1] = 0
            temp_img[i, j, 2] = 0
img = Image.fromarray(temp_img)
img.show()
# bp()
# img.show()
