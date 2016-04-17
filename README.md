# unidice
Unidiceはニコ生でFFXIVのダイスの出目をソートするアプリです。

## スクリーンショット
![スクリーンショット](https://s3-ap-northeast-1.amazonaws.com/unidice/ScreenShot01.jpg)

## インストール
### Windows
ライブラリのインストールが非常に大変なのでバイナリパッケージを配布します。（準備中）
自身でインストールする場合はMacOSのインストールを参考にしてそれぞれWindows版のインストーラをダウンロードしてインストールします。

#### 実行
ダウンロードしたzipファイルを解凍し、unidice.exeを実行します。

### MacOSX
#### 環境
- Python 2.7

##### Qt5
```
$ sudo port install qt5
```
##### PyQt
```
$ sudo port install py27-pyqt5
```
##### tesseract-ocr
macportsでインストールします。Homebrewユーザはコマンドを読み替えてください。
```
$ sudo port install tesseract
```
##### pyocr
依存関係でpillow(PIL fork)が一緒にインストールされます。
```
$ sudo pip install pyocr
```
##### unidiceインストール
```
$ git clone https://github.com/m-sakano/unidice
```
##### tesseractの言語データをコピー
tesseractをソースからインストールした場合は、tessdataのディレクトリが/usr/local/share/tessdataになります。読み替えてください。
```
$ cd unidice
$ sudo cp jpn.tessdata /opt/local/share/tessdata/jpn.tessdata
```
#### 実行
```
$ python unidice.py
```

## ライセンス
本ソフトウェアのライセンスはGPLv3で配布しています。詳細は次の表示をご確認ください。

https://github.com/m-sakano/unidice/blob/master/COPYING

### 概要
- プログラムの利用、修正、配布を行うことができます。
- 再配布の場合はライセンスと著作権の表示、変更点を示すこと、ソースコードの開示が必要です。
- 作者に責任を求めること、再配布にあたり別のライセンスを課すことはできません。

### 依存するソフトウェアおよびライブラリのライセンス

本ソフトウェアが依存するソフトウェアおよびライブラリのライセンスはそれぞれの表示をご確認ください。
本ソフトウェアのバイナリ配布パッケージにはこれらのソフトウェアおよびライブラリを含みます。

#### python
https://docs.python.org/2/license.html

#### Python Imaging Library
http://www.pythonware.com/products/pil/license.htm

#### Qt (GPLv3)
http://doc.qt.io/qt-5/licensing.html

#### PyQt (GPLv3)
Qtのライセンスに依存します。Qtのライセンスをご確認ください。

#### SIP (GPLv3)
https://www.riverbankcomputing.com/software/sip/license

#### pyocr (GPLv3)
https://github.com/jflesch/pyocr/blob/master/COPYING

#### tesseract-ocr (Apache License v2)
https://github.com/tesseract-ocr/tesseract/blob/master/COPYING

#### leptonica
http://leptonica.com/about-the-license.html

## 権利表記
記載されている会社名・製品名・システム名などは、各社の商標、または登録商標です。

## FFXIVの画像に関する著作権表記
Copyright (C) 2010 - 2016 SQUARE ENIX CO., LTD. All Rights Reserved.
