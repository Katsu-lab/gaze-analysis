# 視線情報可視化システム

Bereavement Care実施時の視線情報を可視化するシステム<br>
視線情報の獲得にはアイトラッカを使用

# DEMO

<img width="80%" alt="gaze scatter diagrams" src="assets/img/example2.png">

# Features

* 動画ファイル上にフィルターとして重ねることで，オンラインでのケア実施時のPC画面上における視線を知ることが可能
* 各視線情報の類似度・同期性を表出化する

# Requirement

* python 3.8.5
* pip 22.0.3
* numpy 1.22.2
* matplotlib 3.5.1
* pandas 1.4.1

# Installation

各webサイト参照<br>
基本的にはpipを使用してインストールすればOK

# Usage

appフォルダにて以下のコマンドを実行

```bash
python visualization.py
```

CLIで表示された質問に答えることで視線情報をプロット

データの処理の流れ
1. visualization
2. diagram
3. gaze

**各ファイルの内容**
- app
    - visualization:
    - diagram:
    - gaze:
    - config:
- data
    - gaze_b:
    - gaze_n:

# Note

注意点

# Author

* 福岡 克也 (Katsuya Fukuoka)
* 大阪府立大学 大学院 人間社会システム科学研究科 瀬田研究室
* katsuofukuoka0225@gmail.com

# License

倫理委員会等