import cv2
import numpy as np
import time
import glob
import os


# image_list = sorted(os.listdir('data/check/before'), key=lambda x: int(x.split('.')[0]))
#
# train_img = [('data/check/before/' + file) for file in image_list]
path = r'C:\Users\MVP\Desktop\hehe'
# image_list = sorted(
#     os.listdir(fr'{path}'),
#     key=lambda x: int(x.split('.')[0]))
image_list = os.listdir(path)

train_img = [
    (fr'{path}/' + file)
    for file in image_list]

# build the mapping


def middle(dirs):
    img = cv2.imread(f'{dirs}', 0)
    rev, thresh = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
    # bitwise = cv2.bitwise_not(thresh)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours is not None:
        for cnt in contours:
            if cv2.contourArea(cnt) > 130000:
                print('hehe')
                cv2.drawContours(img, cnt, -1, (0, 0, 0), 3)
                # cv2.imshow('Result', img)
                # cv2.waitKey(0)
                (x, y), radius = cv2.minEnclosingCircle(cnt)
                center = (int(x), int(y))
                radius = int(radius)
                # cv2.circle(img, center, radius, (255, 255, 255), 5)
    return center, radius


def buildMap(Wd, Hd, R1, R2, Cx, Cy):
    map_x = np.zeros((Hd, Wd), np.float32)
    map_y = np.zeros((Hd, Wd), np.float32)
    for y in range(0, int(Hd - 1)):
        for x in range(0, int(Wd - 1)):
            r = (float(y) / float(Hd)) * (R2 - R1) + R1
            theta = (float(x) / float(Wd)) * 2.0 * np.pi
            xS = Cx + r * np.sin(theta)
            yS = Cy + r * np.cos(theta)
            map_x.itemset((y, x), int(xS))
            map_y.itemset((y, x), int(yS))

    return map_x, map_y


# do the unwarping
def unwarp(img, xmap, ymap):
    output = cv2.remap(img, xmap, ymap, cv2.INTER_LINEAR)
    # result = Image(output, cv2image=True)
    # return result
    return output

# st1 ba via canh luc giac, mop me canh luc giac
# x = 500
# y = 500
# vals = [[x, y], [x + 370, y], [x + 500, y]]

# st1 tray, ba via mat dau

# st1 tray, ba via mat luc giac
# x = 500
# y = 500
# vals = [[x, y], [x + 308, y], [x + 500, y]]

# st1 mop me mat dau lg op2
# x = 500
# y = 500
# vals = [[x, y], [x + 219, y], [x + 411, y]]

# st2 van dao phi 15, 14
# x = 1320
# y = 945
# vals = [[x, y], [x + 320, y], [x + 960, y]]     # phi 15
# vals = [[x, y], [x + 210, y], [x + 978, y]]     # phi 14

# st3 bac, sot tho 10.4
# x = 1365
# y = 938
# vals = [[x, y], [x + 378, y], [x + 634, y]]     # phi 10.4

# st3 tray, ba via 10.4
# x = 1365
# y = 938
# vals = [[x, y], [x + 366, y], [x + 654, y]]     # phi 10.4

# st3 ba via c03
# x = 1353
# y = 933
# vals = [[x, y], [x + 190, y], [x + 318, y]]   # c03

# st5
# x = 500
# y = 500
# vals = [[x, y], [x + 226, y], [x + 354, y]]     # ba via 3.7
# vals = [[x, y], [x + 136, y], [x + 264, y]]     # ba via mat dau op1
# vals = [[x, y], [x + 130, y], [x + 290, y]]     # mop me mat dau op1
# vals = [[x, y], [x + 231, y], [x + 359, y]]     # loi bac 3.7 den thap
# vals = [[x, y], [x + 340, y], [x + 500, y]]     # mop me luc giac op1, bia via mat luc giac

# st7
x = 1331
y = 955
# vals = [[x, y], [x + 576, y], [x + 960, y]]     # can_lom_be_mat_luc_giac, di_vat_be_mat_luc_giac
# vals = [[x, y], [x + 612, y], [x + 836, y]]     # bavia canh luc giac op1
vals = [[x, y], [x + 698, y], [x + 922, y]]     # bavia canh luc giac op2

last = (0, 0)
Cx = vals[0][0]
Cy = vals[0][1]
R1x = vals[1][0]
R1y = vals[1][1]
R1 = R1x - Cx
R2x = vals[2][0]
R2y = vals[2][1]
R2 = R2x - Cx
Wd = int(2.0 * ((R2 + R1) / 2) * np.pi)
Hd = (R2 - R1)
xmap, ymap = buildMap(Wd, Hd, R1, R2, Cx, Cy)

np.save(r'C:\Users\MVP\Desktop\HS0010_version_2\build_maps\station_7/xmap_bavia_canh_lg_op2.npy', xmap)
np.save(r'C:\Users\MVP\Desktop\HS0010_version_2\build_maps\station_7/ymap_bavia_canh_lg_op2.npy', ymap)
# xmap = np.load(r'C:\Users\MVP\Desktop\HS0010_version_2\build_maps\station_1/bavia_canh_lg_xmap.npy')
# ymap = np.load(r'C:\Users\MVP\Desktop\HS0010_version_2\build_maps\station_1/bavia_canh_lg_ymap.npy')
# for count, lists in enumerate(train_img, 1):

# img = cv2.imread(r'C:\Users\MVP\Downloads\data_2403\data_2403\mm_md_op2/1.jpg', 0)
# result = unwarp(img, xmap, ymap)
# cv2.imwrite(fr'C:\Users\MVP\Desktop\hehe/hhihihi.jpg', result)

# result = cv2.resize(result, (4544, 224))
# cv2.imshow('Input', im)
# cv2.imshow('Result', result)
# cv2.waitKey(0)


