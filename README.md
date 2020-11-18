# Banana and Nasu
食べ物を見て、好き嫌いを発話するパッケージ

## Directory structure
* launch
    * camera.launch
        * カメラ映像を写すロンチファイル
    * banana_and_nasu.launch
        * バナナとナスを認識して、好き嫌いを発話するロンチファイル
* scripts
    * images
        * banana.jpg
            * バナナの画像
        * camera.jpg
            * カメラ画像(banana_and_nasu.launchの実行後に画像が保存される)
        * nasu.jpg
            * ナスの画像
    * kasamashi_images(kasamashi.pyの実行後にフォルダと画像が保存される)
        * kasamashi1.jpg
        * kasamashi2.jpg
        * kasamashi3.jpg
        * kasamashi4.jpg
    * detect_banana_and_nasu.py
        * バナナとナスを認識するプログラム
    * kasamashi.py
        * データセットを増やすプログラム
    * likes_and_dislikes.py
        * カメラ画像からバナナとナスを認識して、発話するプログラム
    * speech.py
        * 音声合成をするプログラム
    * translate.py
        * 文章を翻訳するプログラム
* CMakeLists.txt
    * ROSパッケージの設定ファイル
* package.xml
    * ROSパッケージの設定ファイル
* LICENCE
    * ROSパッケージのライセンスファイル
* README.md
    * パッケージの説明書

## Requirements
* [uvc_camera](http://wiki.ros.org/uvc_camera)

## Installation

```
cd ~/catkin_ws
rosdep install -r -y -i --from-paths src
```

## Usage
* カメラ映像を写す
```sh
roslaunch banana_and_nasu camera.launch
```
* バナナとナスを認識して、発話する
```sh
roslaunch banana_and_nasu banana_and_nasu.launch
```