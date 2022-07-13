import cv2
import numpy as np
import os

path = r'C:\Users\AVN\Desktop\hehe'
# image_list = sorted(
#     os.listdir(fr'{path}'),
#     key=lambda x: int(x.split('.')[0]))
image_list = os.listdir(path)

train_img = [
    (fr'{path}/' + file)
    for file in image_list]


for count, (image, lists) in enumerate(zip(image_list, train_img), 1):
    img = cv2.imread(lists, 0)
    img = cv2.resize(img, (2880-256, 128))

    img = img[:, 1:img.shape[1] - 1].astype('uint8')
    left = img[:, :127].astype('uint8')
    right = img[:, img.shape[1] - 128:].astype('uint8')

    result = cv2.hconcat([img, left])
    result = cv2.hconcat([right, result])
    result = cv2.resize(result, (img.shape[1]+258, img.shape[0]))

    cv2.imwrite(rf'{path}/{image}', result)

    # cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('Image', (2560, 192))
    # cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('Result', (2816, 192))
    # cv2.imshow('Result', result)
    # cv2.imshow('Image', img)
    #
    # cv2.waitKey(0)


