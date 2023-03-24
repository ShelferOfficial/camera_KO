#https://dev.classmethod.jp/articles/opencv-preprocess-for-ml-training/
from pathlib import Path
import pathlib
from tqdm import tqdm
import cv2
input_path = pathlib.Path('/home/shelfer/Desktop/KO/input')
output_path = pathlib.Path('/home/shelfer/Desktop/KO/output-boxed')
output_path.mkdir(parents=True, exist_ok=True)

output_path_debug = pathlib.Path('/home/shelfer/Desktop/KO/output-boxed-debug')
output_path_debug.mkdir(parents=True, exist_ok=True)

PADDING = 15

for p in tqdm(input_path.glob('foo-otsu-tri.png'), total=len(list(input_path.glob('foo-otsu-tri.png'))), ascii=True):

    img = cv2.imread(str(p))

    # グレースケール
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("wahaha.png",img_gray)

    # 2値化
    _, im_bw = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 輪郭検出
    contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 画像内の輪郭の端を探す
    edge_l, edge_r, edge_t, edge_b = 1e10, 0, 1e10, 0
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])

        edge_l = x   if edge_l > x   else edge_l
        edge_r = x+w if edge_r < x+w else edge_r
        edge_t = y   if edge_t > y   else edge_t
        edge_b = y+h if edge_b < y+h else edge_b

    # padding + limitter
    edge_t = edge_t - PADDING if edge_t - PADDING > 0            else 0
    edge_b = edge_b + PADDING if edge_b + PADDING < img.shape[0] else img.shape[0]
    edge_l = edge_l - PADDING if edge_l - PADDING > 0            else 0
    edge_r = edge_r + PADDING if edge_l + PADDING < img.shape[1] else img.shape[1]

    # デバッグのためboxを画像内に描画
    img_con = img.copy()
    img_con = cv2.rectangle(img_con, (edge_l, edge_t), (edge_r, edge_b), (0, 255, 0), cv2.LINE_4)
    cv2.imwrite(str(output_path_debug.joinpath(p.name)), img_con)

    # 切り出し画像を出力
    img_boxed = img[edge_t:edge_b,edge_l:edge_r]
    cv2.imwrite(str(output_path.joinpath(p.name)), img_boxed)