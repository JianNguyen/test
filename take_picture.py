import cv2
from vimba import *


count = 11
with Vimba.get_instance() as vimba:
    cams = vimba.get_all_cameras()
    with cams[0] as cam:
        while True:
            camera = cam.get_frame()
            frame = camera.as_opencv_image()
            show = cv2.resize(frame, (800, 572))
            cv2.imshow('Frame', show)
            # key = cv2.waitKey(0)q
            if cv2.waitKey(1) & 0xFF == ord('t'):
                resized = cv2.resize(frame, (1600, 1152), interpolation=cv2.INTER_AREA)
                cv2.imwrite(f"C:/Users/84386/Desktop/Giang/DATA1/kros1/Part{count}.jpg", resized)
                print('OK!', count)
                count = count + 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cv2.destroyAllWindows()
