import cv2
import os
import numpy as np

path = r'C:\Users\AVN\Desktop\gg\SegmentationClass'
image_list = os.listdir(path)
train_img = [(fr'{path}/' + file) for file in image_list]

for count, (lists, image) in enumerate(zip(train_img, image_list), 1):
    img = cv2.imread(lists, 1)
    # img = cv2.resize(img, (192, 512))
    # print(lists)
    # print(image)

    img[np.where((img != [255, 0, 255]).all(axis=2))] = [0, 0, 0]
    img[np.where((img == [255, 0, 255]).all(axis=2))] = [255, 255, 255]

    # img[np.where((img != [255, 255, 255]).all(axis=2))] = [0, 0, 0]
    # img[np.where((img == [255, 255, 255]).all(axis=2))] = [255, 0, 255]

    # img[np.where((img != [255, 255, 255]).all(axis=2))] = [0, 0, 0]
    # img[np.where((img == [255, 255, 255]).all(axis=2))] = [128, 0, 128]

    # img[np.where((img == [255, 221, 51]).all(axis=2))] = [0, 0, 0]
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.resize(img, (192, 512))
    # cv2.imwrite(fr'C:\Users\AVN\Desktop\gg\SegmentationClass/{image}', img)
    cv2.imwrite(fr'C:\Users\AVN\Desktop\hehe/{image}', img)
    # cv2.imshow('Red', img)
    # cv2.waitKey(0)
    # number += 1
    # if number == 177:
    #     break
# number = 91
# img = cv2.imread(r'C:\Users\84386\Desktop\Nha-san\Semantic-Shapes-master\dataset\straight\83.png', 0)
# for count in range(100):
#     cv2.imwrite(
#         fr'C:\Users\84386\Desktop\Nha-san\Semantic-Shapes-master\dataset\straight\mask_scratch_train\{number}.png', img)
#     if number == 176:
#         break
#     number += 1
