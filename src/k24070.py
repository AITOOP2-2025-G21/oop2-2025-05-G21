import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def k24070():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # capture_img : cv2.Mat = "implement me"

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    # カメラ画像をグリッド状に並べる
    new_capture_img = np.zeros_like(google_img)
    for y in range(0, g_hight, c_hight):
        for x in range(0, g_width, c_width):
            end_y = min(y + c_hight, g_hight)
            end_x = min(x + c_width, g_width)
            tile_h = end_y - y
            tile_w = end_x - x
            new_capture_img[y:end_y, x:end_x] = capture_img[0:tile_h, 0:tile_w]
        
    for x in range(g_width):
        for y in range(g_hight):
            b1, g1, r1 = google_img[y, x]
            b2, g2, r2 = new_capture_img[y, x]  # ← capture_img ではなく new_capture_img を使う

            # もし白色(255,255,255)だったら置き換える
            if (b1, g1, r1) == (255, 255, 255):
                google_img[y, x] = b2, g2, r2

    # 書き込み処理
    cv2.imwrite('output_images/lecture05_01', google_img)
