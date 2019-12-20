import numpy as np
import cv2
import sys
import argparse

parser = argparse.ArgumentParser(description='Turn your anime picture into a wallpaper')

parser.add_argument('If', metavar='source image', type=str, help='image to be converted to a wallpaper')
parser.add_argument('Of', metavar='destination image image', type=str, help='file where the image will be saved')
parser.add_argument("-V", default = False, action='store_true', help = "Place the source image on the top, instead of the bottom")
parser.add_argument("-H", default = False, action='store_true', help = "Place the source image on the left, instead of the right")
parser.add_argument("-f", default = False, action='store_true', help = "Flip source image by a vertical axis")
parser.add_argument("-F", default = False, action='store_true', help = "Flip source image by a horizontal axis")


args = parser.parse_args()

print(args.If)

Img = cv2.imread(args.If[3:])


Resolution = (1080, 1920)
MakeBorderArgs = [0 for i in range(4)]

if args.f:
    Img = cv2.flip(Img, 1)

if args.F:
    Img = cv2.flip(Img, 0)
    
if args.V: #store the image on the top
    MakeBorderArgs[1] = Resolution[0] - Img.shape[0]
else:
    MakeBorderArgs[0] = Resolution[0] - Img.shape[0]

if args.H: #store the image on the left
    MakeBorderArgs[3] = Resolution[1] - Img.shape[1]
else:
    MakeBorderArgs[2] = Resolution[1] - Img.shape[1]


Img = cv2.copyMakeBorder(Img, *MakeBorderArgs, cv2.BORDER_REPLICATE)

print(args.Of[3:])

cv2.imwrite(args.Of[3:], Img)
