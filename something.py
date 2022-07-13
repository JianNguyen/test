import cv2
import numpy as np
import os

path = r'C:\Users\MVP\Desktop\HS0010_version_2\new_dataset\st1_ta_lg_op2\image_val_mask'
# image_list = sorted(
#     os.listdir(fr'{path}'),
#     key=lambda x: int(x.split('.')[0]))
image_list = os.listdir(path)

train_img = [
    (fr'{path}/' + file)
    for file in image_list]

for count, (image, lists) in enumerate(zip(image_list, train_img), 1):
    img = cv2.imread(lists, 0)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if contours is not None:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 200:
                cv2.drawContours(img, [cnt], -1, (0, 0, 0), -1)
                cv2.imwrite(rf'C:\Users\MVP\Desktop\HS0010_version_2\new_dataset\st1_ta_lg_op2\image_val_mask/{image}', img)