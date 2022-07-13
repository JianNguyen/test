import numpy as np
import cv2
from imgaug import augmenters as iaa
import os

seq = iaa.Sequential([
    iaa.Fliplr(0.5),
    # iaa.Add((-10, 10)),
    # iaa.MedianBlur(k=(1, 5)),
    # iaa.Affine(rotate=(-1, 1)),
    # iaa.Pad(px=((0, 50), (0, 150), (0, 50), (0, 150)))
    # iaa.GaussianBlur(sigma=(2, 5.0))
    # iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.08 * 255), per_channel=0.5)
], random_order=True)
# train_img = [(r'C:\Users\84386\Desktop\Nha-san\MultiClass-Semantic-Shapes-master\dataset\straight_2\mask_bavia_train/' + file)
#              for file in
#              os.listdir(r'C:\Users\84386\Desktop\Nha-san\MultiClass-Semantic-Shapes-master\dataset\straight_2\mask_bavia_train')
#              if
#              file.endswith('.png')]
# image_list = sorted(
#     os.listdir(r'C:\Users\MVP\Desktop\hehe'),
#     key=lambda x: int(x.split('.')[0]))
image_list = os.listdir(r'C:\Users\MVP\Desktop\hehe')

train_img = [
    (r'C:\Users\MVP\Desktop\hehe/' + file)
    for file in image_list]
# print(train_img)
for count, lists in enumerate(train_img, 109):
    img = cv2.imread(lists, 0)
    flip_1 = np.fliplr(img)
    # cv2.imshow('hehe', img)
    # shape = [192, 1536, 1]
    # seq_det = seq.to_deterministic()
    # image_aug = seq_det.augment_images([img])[0]
    # image_aug = np.expand_dims(image_aug, axis=2)
    # print(image_aug.shape)
    # cv2.imshow('In', img)
    # cv2.imshow('Frame', flip_1)
    # cv2.waitKey(0)
    cv2.imwrite(fr'C:\Users\MVP\Desktop\hehe\OK_{count}.jpg', flip_1)
    # cv2.imshow('Frame', flip_1)
    # cv2.waitKey(0)
    # x = tf.placeholder(dtype=tf.float32, shape=shape)
