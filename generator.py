import numpy as np
import cv2


def GetBackround(Image):
    return Image[0][0]

Resolution = (1080, 1920)

Img = cv2.imread('test.jpg')
Wallpaper = np.zeros((*Resolution, 3), np.uint8)


Background = GetBackround(Img)
for i in range(Resolution[0]):
    for j in range(Resolution[1]):
        Wallpaper[i][j] = Background 

for i in range(Img.shape[0]):
    for j in range(Img.shape[1]):
        Wallpaper[Resolution[0]-i-1][Resolution[1]-j-1] = Img[Img.shape[0]-i-1][Img.shape[1]-j-1]


cv2.imwrite("output.jpg", Wallpaper)
