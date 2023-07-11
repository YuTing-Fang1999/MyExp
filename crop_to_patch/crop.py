import cv2
import numpy as np
import os

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("The", path, "dir is created!")

mkdir("crop_patch")

dir = "align/"
    
img0 = cv2.imread(dir+os.listdir(dir)[0])
H,W,C = img0.shape
resolution = 256


shift = resolution//2
shift_down_right = []
down = 256
right = 256
while down<H:
    right = 256
    while right<W:
        shift_down_right.append([down, right])
        right+=shift
    down+=shift
print(len(shift_down_right))

for j, f in enumerate(os.listdir(dir)):
    print(dir+f)
    img = cv2.imread(dir+f)
    for i, down_right in enumerate(shift_down_right):
        down, right = down_right
        crop_patch = img[down-resolution:down, right-resolution:right, :]
        cv2.imwrite('crop_patch/{}_{}.jpg'.format(i, j), crop_patch)