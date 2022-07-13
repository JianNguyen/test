import numpy as np
import cv2
import os
import math
import time
# cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Frame', 800, 576)
# image_list = sorted(
#     os.listdir(r'C:\Users\84386\Desktop\Nha-san\MultiClass-Semantic-Shapes-master\dataset\test_straight_2\before'),
#     key=lambda x: int(x.split('.')[0]))
path = r'C:\Users\MVP\Desktop\HS0010_version_2\dataset\st7_o_vang_be_mat_luc_giac/test/ng'
address_save_path = r'C:\Users\MVP\Desktop\HS0010_version_2\dataset\st7_o_vang_be_mat_luc_giac\result'
image_list = os.listdir(path)
train_img = [
    (path + '/' + file)
    for file in image_list]
#
# for dirs in range(1):
#     # img = cv2.imread(f'{dirs}', 0)
#     img = cv2.imread('data/before/83.jpg', 0)
#     rev, thresh = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
#     bitwise = cv2.bitwise_not(thresh)
#     cv2.imshow('Frame', bitwise)
#     cv2.waitKey(0)
#     contours, hierarchy = cv2.findContours(bitwise, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     if contours is not None:
#         for cnt in contours:
#             if cv2.contourArea(cnt) > 3500:
#                 # cv2.drawContours(img, contours, -1, (255, 255, 255), 5)
#                 (x, y), radius = cv2.minEnclosingCircle(cnt)
#                 center = (int(x), int(y))
#                 radius = int(radius)
#                 cv2.circle(img, center, radius-20, (255, 255, 255), 5)
#                 cv2.circle(img, center, radius+170, (255, 255, 255), 5)
#
#     cv2.imshow('Frame', img)
#     cv2.waitKey(0)

# detected_circles = cv2.HoughCircles(thresh,
#                                     cv2.HOUGH_GRADIENT, 1, 20, param1=50,
#                                     param2=30, minRadius=1, maxRadius=40)
# # result = np.where(im > 0, [255, 0])
# if detected_circles is not None:
#     for pt in detected_circles[0, :]:
#         a, b, r = pt[0], pt[1], pt[2]
#
#         # Draw the circumference of the circle.
#         cv2.circle(img, (a, b), r, (0, 255, 0), 2)
#
#         # Draw a small circle (of radius 1) to show the center.
#         cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
#         cv2.imshow("Detected Circle", img)
#         cv2.waitKey(0)

speed_sum = 0
total = len(image_list)
wrong_number = 0
datas = []
hsv_color1 = np.asarray([10, 100, 10])   # white!
hsv_color2 = np.asarray([30, 150, 30])   # yellow! note the order
for count, (image, lists) in enumerate(zip(image_list, train_img), 1):
    speed = time.perf_counter()

    img = cv2.imread(lists, 1)   # you can read in images with opencv
    crop = img[80:320, :].astype('uint8')
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    crop = cv2.blur(crop, (11, 11))
    imgHLS = cv2.cvtColor(crop, cv2.COLOR_BGR2HLS)
    mask = cv2.inRange(imgHLS, hsv_color1, hsv_color2)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours is not None:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 800:
                cv2.drawContours(mask, [cnt], -1, (0, 0, 0), -1)
    cv2.imshow('hehe', mask)
    cv2.waitKey(0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    close = 255 - cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    close = cv2.bitwise_not(close)

    contours, hierarchy = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    bit_area = False
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            bit_area = True
            # cv2.drawContours(img, [cnt], 0, (0, 0, 255), 3)
    if bit_area:
        wrong_number += 1
        datas.append(f'{image}-->False')
    else:
        datas.append(f'{image}-->True')
    # result = cv2.vconcat([gray, close])
    speed_sum += time.perf_counter() - speed
    print(time.perf_counter()-speed)
    # cv2.imwrite(fr'{address_save_path}/{image}', result)
    # cv2.namedWindow('out', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('out', (4800, 240))
    # cv2.imshow('out', close)
    # cv2.namedWindow('in', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('in', (4800, 384))
    # cv2.imshow('in', img)
    # cv2.waitKey(0)
print('trung binh: ', speed_sum / total)
print(f'Ti le:  {wrong_number}/{total}')
with open(r'C:\Users\MVP\Desktop\HS0010_version_2\dataset\st7_o_vang_be_mat_luc_giac\result_ok.txt', 'w') as f:
    for data in datas:
        f.write(data)
        f.write('\n')
    f.write(f'{wrong_number}/{total}')
    f.write('\n')
    f.write(f'trung binh: {speed_sum/total}')