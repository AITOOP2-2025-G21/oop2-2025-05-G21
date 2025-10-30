import numpy as np
import cv2
from my_module.k24084.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = app.get_img()

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape

    for x in range(g_width):
        for y in range(g_hight):
            b, g, r = google_img[y, x]
            if (b, g, r) == (255, 255, 255):
                cx = x % c_width
                cy = y % c_hight
                google_img[y, x] = capture_img[cy, cx]

    # 書き込み処理
    cv2.imwrite('lecture05_01_K24084.png', google_img)

if __name__ == "__main__":
    lecture05_01()
