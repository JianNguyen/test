import random
from imgaug import augmenters as iaa
import cv2
import os
import numpy as np

seq = iaa.Sequential([
    iaa.Fliplr(0.5),
    # iaa.Add((-10, 10)),
    # iaa.MedianBlur(k=(1, 5)),
    iaa.Affine(rotate=(-1, 1)),
    # iaa.Pad(px=((0, 30), (0, 450), (0, 30), (0, 450)))
], random_order=True)


def agu_giang(img, a):
    img = img[:, 249:img.shape[1] - 249].astype("uint8")
    x1 = img[:, :64 * a].astype('uint8')
    x2 = img[:, 64 * a:].astype('uint8')
    img = cv2.hconcat([x2, x1])

    img = img[:, 1:img.shape[1] - 1].astype('uint8')
    left = img[:, :248].astype('uint8')
    right = img[:, img.shape[1] - 249:].astype('uint8')

    result = cv2.hconcat([img, left])
    result = cv2.hconcat([right, result])
    result = cv2.resize(result, (img.shape[1] + 249*2+2, img.shape[0]))

    return result


def agu_mask_giang(img, a):
    img = img[:, 249:img.shape[1] - 249].astype("uint8")
    x1 = img[:, :64 * a].astype('uint8')
    x2 = img[:, 64 * a:].astype('uint8')
    img = cv2.hconcat([x2, x1])

    img = img[:, 1:img.shape[1] - 1].astype('uint8')
    left = img[:, :248].astype('uint8')
    right = img[:, img.shape[1] - 249:].astype('uint8')

    result = cv2.hconcat([img, left])
    result = cv2.hconcat([right, result])
    result = cv2.resize(result, (img.shape[1] + 249*2+2, img.shape[0]))

    contours, _ = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if contours is not None:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area <= 450:
                cv2.drawContours(result, [cnt], -1, (0, 0, 0), -1)
    return result


path = r'C:\Users\AVN\Desktop\train'
images = os.listdir(fr'{path}')
train_img = [(fr'{path}/' + file) for file in os.listdir(fr'{path}') if file.endswith('.jpg')]

path_1 = r'C:\Users\AVN\Desktop\mask'
images_1 = os.listdir(fr'{path_1}')
train_img_1 = [(fr'{path_1}/' + file) for file in os.listdir(fr'{path_1}') if file.endswith('.png')]

a = [15, 35]
num_train = 1
num_mask = 1
for i in a:
    for count, (image, lists) in enumerate(zip(images, train_img), 59):
        img = cv2.imread(lists, 0)
        img = agu_giang(img, i)
        cv2.imwrite(rf"C:\Users\AVN\Desktop\pic/add_{num_train}.jpg", img)
        if i == 35:
            img = np.fliplr(img)
        cv2.imwrite(rf"C:\Users\AVN\Desktop\pic/add_{num_train}.jpg", img)
        num_train += 1


for i in a:
    for count1, (image1, lists1) in enumerate(zip(images_1, train_img_1), 59):
        img = cv2.imread(lists1, 0)
        img = agu_mask_giang(img, i)
        if i == 35:
            img = np.fliplr(img)
        cv2.imwrite(rf"C:\Users\AVN\Desktop\pic/add_{num_mask}.png", img)
        num_mask += 1
