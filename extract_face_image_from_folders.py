"""
This script extracts all images from the original lfw image dataset into one folder
"""

import os

lfw = './lfw'
destination = './raw'

folders = os.listdir(lfw)
print folders

for i in range(len(folders)):
    imgs = os.listdir(lfw + '/' + folders[i])
    for j in range(len(imgs)):
        img_name = imgs[j]
        os.rename(lfw + '/' + folders[i] + '/' + img_name, destination + '/' + img_name)

