import numpy as np
import cv2
import os

path = r'D:\#GIANG\HS0010_version_2\improve_dataset\test_st9_khuyet_phi_1864\image_train/OK_1.jpg'
img = cv2.imread(path, 0)
img_mask = np.zeros_like(img)
count = 224
while count < 366:
    cv2.imwrite(fr'C:\Users\AVN\Desktop\hehe\OK_{count}.png', img_mask)
    count += 1





# image_list = sorted(
#     os.listdir(r'C:\Users\MVP\Desktop\hehe'),
#     key=lambda x: int(x.split('.')[0]))
# cv2.namedWindow('hehe', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('hehe', 4800, 384)
# image_list = os.listdir(r'C:\Users\MVP\Desktop\aa\New folder')
#
# train_img = [
#     (r'C:\Users\MVP\Desktop\aa\New folder/' + file)
#     for file in image_list]
# hsv_color1 = np.asarray([180, 0, 20])  # white!
# hsv_color2 = np.asarray([255, 40, 80])  # yellow! note the order
# for count, (lists, image) in enumerate(zip(train_img, image_list), 1):
#     img = cv2.imread(lists, 1)
#     # cv2.imshow('hehe', img)
#     # cv2.waitKey(0)
#     mask = cv2.inRange(img, hsv_color1, hsv_color2)
#     cv2.imwrite(fr'C:\Users\MVP\Desktop\hihi\{image}', mask)
#     # cv2.imshow('hehe', mask)
#     # cv2.waitKey(0)
