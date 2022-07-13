import os
import natsort
import cv2


# Function to rename multiple files
def main():
    folder = r'C:\Users\AVN\Desktop\hehe'
    # alist = sorted(
    #     os.listdir(r'C:\Users\MVP\Desktop\HS0010_version_2\dataset\st2_rung_dao_phi_14\image_train_mask'),
    #     key=lambda x: int(x.split('.')[0]))
    alist = os.listdir(folder)
    sort = natsort.natsorted(alist, reverse=False)
    # path = r'C:\Users\MVP\Desktop\dataset\bavia_c03\after_ok'
    # image_list = os.listdir(path)
    train_img = [
        (fr'{folder}/' + file)
        for file in alist]
    # print(train_img)
    # alist.sort(key=lambda f: int(filter(str.isdigit, f)))
    number = 1
    for count, filename in enumerate(train_img, 1):
        dst = f"{str(count)}.jpg"
        src = f"{filename}"
        dst = f"{folder}/{dst}"
        os.rename(src, dst)
        number += 1


if __name__ == '__main__':
    main()
