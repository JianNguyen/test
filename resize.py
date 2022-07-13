import cv2
import os
import numpy as np
import random


def agu_giang(img, a):
    img = img[:, 128:img.shape[1] - 128].astype("uint8")
    x1 = img[:, :64 * a].astype('uint8')
    x2 = img[:, 64 * a:].astype('uint8')
    result = cv2.hconcat([x2, x1])

    left = result[:, :128].astype('uint8')
    right = result[:, img.shape[1] - 128:].astype('uint8')

    result = cv2.hconcat([result, left])
    result = cv2.hconcat([right, result])
    return result
path = r'C:\Users\AVN\Desktop\c'
path_2 = r'C:\Users\AVN\Desktop\hehe'
image_list = os.listdir(path)
image_list_2 = os.listdir(path_2)
# image_list = sorted(
#     os.listdir(fr'{path}'),
#     key=lambda x: int(x.split('.')[0]))
train_img = [(fr'{path}/' + file) for file in image_list]
train_img_2 = [(fr'{path_2}/' + file) for file in image_list_2]


for count, (lists, lists_2) in enumerate(zip(train_img, train_img_2), 1):
    print(lists)
    print(lists_2)
    img = cv2.imread(lists, 0)
    img_2 = cv2.imread(lists_2, 0)
    a = random.randint(1, int(img.shape[1]/64) - 1)
    img = agu_giang(img, a)
    img_2 = agu_giang(img_2, a)

    final = cv2.vconcat([img, img_2])
    cv2.imwrite(fr'C:\Users\AVN\Desktop\a/{count}.jpg', final)
    # cv2.imshow('hehe', img)
    # cv2.waitKey(0)
