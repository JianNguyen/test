import imageio
import os
import cv2

path = r'C:\Users\AVN\Desktop\4_0_0'
image_list = os.listdir(path)
train_img = [(fr'{path}/' + file) for file in image_list]

count = 1
for path in train_img:
    gif = imageio.get_reader(uri=path, mode="I")
    for frame in gif:
        cv2.imwrite(fr'C:\Users\AVN\Desktop\hehe/{count}.jpg', frame)
        count += 1
