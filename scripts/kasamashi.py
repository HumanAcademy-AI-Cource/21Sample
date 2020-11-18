#!/usr/bin/env python
# -*- coding: utf-8 -*

# ライブラリのインポート
import cv2
import os

def kasamashi(path, deg, scale):
    """
    かさ増し画像を生成する関数
    """
    
    image = cv2.imread(path)

    # 画像の回転準備
    target = (int(image.shape[1] / 2), int(image.shape[0] / 2))
    matrix = cv2.getRotationMatrix2D(target, deg, scale)

    # 画像を変換して返す
    return cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

# かさ増し画像を保存するフォルダの名前
dirname = "./kasamashi_images"

# かさ増し画像を保存するフォルダがなければ作成
if not os.path.isdir(dirname):
    os.mkdir(dirname)

# かさ増しする画像
image_path = "./images/nasu.jpg"

# かさ増し画像を生成(パラメータ: 角度, 拡大率)
print("かさ増し画像の生成開始")
image1 = kasamashi(image_path, 45, 1.0)
image2 = kasamashi(image_path, 90, 0.7)
image3 = kasamashi(image_path, -45, 1.0)
image4 = kasamashi(image_path, 0, 1.5)

# かさ増し画像を保存
print("かさ増し画像を保存（{}に保存）".format(dirname))
cv2.imwrite(dirname + "/kasamashi1.jpg", image1)
cv2.imwrite(dirname + "/kasamashi2.jpg", image2)
cv2.imwrite(dirname + "/kasamashi3.jpg", image3)
cv2.imwrite(dirname + "/kasamashi4.jpg", image4)