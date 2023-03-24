#https://dev.classmethod.jp/articles/opencv-preprocess-for-ml-training/
from pathlib import Path
import pathlib
#import glob
from tqdm import tqdm
import cv2
#import tqdm
input_path = pathlib.Path('/home/shelfer/Desktop/KO/output-boxed')
output_path = pathlib.Path('/home/shelfer/Desktop/KO/output-resized')
output_path.mkdir(parents=True, exist_ok=True)

# まずは最大幅width_maxを求める
width_max = 0
for p in tqdm(input_path.glob('foo-otsu.png'), total=len(list(input_path.glob('foo-otsu.png'))), ascii=True):

    img = cv2.imread(str(p))

    width_max = img.shape[1] if width_max < img.shape[1] else width_max

# これを最終的なリサイズ後の幅とする
width_target = width_max

# 関数定義
def scale_to_width(img, width):
    """
    アスペクト比を維持した状態で幅合わせする処理
    """
    h, w = img.shape[:2]
    height = round(h * (width / w))
    dst = cv2.resize(img, dsize=(width, height))
    return dst

# アスペクト比を維持した状態でwidth_maxに合わせた場合の最小の高さheight_minを求める。
height_min = 1e10
for p in tqdm(input_path.glob('foo-otsu.png'), total=len(list(input_path.glob('foo-otsu.png'))), ascii=True):

    img = cv2.imread(str(p))

    img_resize = scale_to_width(img, width_target)

    height_min = img_resize.shape[0] if height_min > img_resize.shape[0] else height_min

# これを最終的なリサイズ後の高さとする
height_target = height_min

# リサイズ実行
for p in tqdm(input_path.glob('foo-otsu.png'), total=len(list(input_path.glob('foo-otsu.png'))), ascii=True):

    img = cv2.imread(str(p))

    img_resize = scale_to_width(img, width_target)

    # 高さの差分は上下均等に割り当てる
    height_diff = img_resize.shape[0] - height_target
    img_resize = img_resize[height_diff//2:height_diff//2+height_min]

    # 出力
    cv2.imwrite(str(output_path.joinpath(p.name)), img_resize)