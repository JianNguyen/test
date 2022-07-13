import numpy as np
import time
import cv2
import os
path_1 = r'C:\Users\AVN\Desktop\hehe'
path = r'C:\Users\AVN\Desktop\mask'
# image_list = sorted(
#     os.listdir(fr'{path}'),
#     key=lambda x: int(x.split('.')[0]))
image_list = os.listdir(path)

train_img = [
    (fr'{path}/' + file)
    for file in image_list]

area_val = []
for count, (lists, image) in enumerate(zip(train_img, image_list), 1):
    img = cv2.imread(lists, 0)
    # result = img[900:1284, :]  # dong dau ren
    # result = img[:, :2880]
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if contours is not None:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area == 476:
                print(image)
            if area > 26:
                # cv2.drawContours(img, [cnt], -1, (0, 0, 0), -1)
                # print(image)
                area_val.append(area)

    # result = cv2.resize(img, (2560, 128))
    # new1 = img[16:int(img.shape[0]-16), :]

    # cv2.imwrite(rf'{path}\{image}', result)

    # cv2.imshow('Frame1', result)
    # cv2.waitKey(0)

# # img = cv2.imread('hai.jpg', 0)
# # a = time.time()
# # img = cv2.resize(img, (3200, 2304))
print('Min area: ', min(area_val))

# img1 = cv2.imread('5.jpg', 0)
# new1 = img1[:, 0:1500].astype('uint32')
# img2 = cv2.imread('6.jpg', 0)
# new2 = img2[:, 0:1500].astype('uint32')
# avg = (new1 + new2)/2
# newarr = avg.astype('uint8')
# #
# #
# cv2.imshow('Frame1', newarr)
# cv2.imshow('Frame2', img1)
# cv2.imshow('Frame3', img2)
# cv2.waitKey(0)





# path = r'C:\Users\MVP\Downloads\data_0704\data_0704\tray_bv_phi10'
# image_list = sorted(
#     os.listdir(fr'{path}'),
#     key=lambda x: int(x.split('.')[0]))
# # image_list = os.listdir(path)
#
# train_img = [
#     (fr'{path}/' + file)
#     for file in image_list]
#
# sumx = 0
# count = 0
# sumy = 0
# for lists in train_img:
#     img = cv2.imread(fr'{lists}', 0)
#     rev, thresh = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
#     # bitwise = cv2.bitwise_not(thresh)
#     # cv2.imshow('hehe', thresh)
#     # cv2.waitKey(0)
#     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     if contours is not None:
#         for cnt in contours:
#             if cv2.contourArea(cnt) > 20000:
#                 count += 1
#                 cv2.drawContours(img, cnt, -1, (0, 0, 0), 3)
#                 # cv2.imshow('Result', img)
#                 # cv2.waitKey(0)
#                 (x, y), radius = cv2.minEnclosingCircle(cnt)
#                 center = (int(x), int(y))
#                 print(int(x))
#                 print(int(y))
#                 sumy += int(y)
#                 sumx += int(x)
#                 radius = int(radius)
#                 # cv2.circle(img, center, radius, (255, 255, 255), 5)
# print('sumx: ', sumx/count)
# print('sumy: ', sumy/count)
# print(count)
