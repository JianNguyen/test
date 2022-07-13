import cv2
import os
path_1 = r'C:\Users\AVN\Desktop\hehe'
path = r'C:\Users\AVN\Desktop\hehe'
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
    result = img[:, :3488]
    cv2.imwrite(f"{path_1}/{image}", result)