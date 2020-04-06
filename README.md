# GUI_for_matplotlib
GUI application using matplotlib

MATPLOTはGUIを用いて簡単に２次元グラフをかけるコードです。
また、一度描いたグラフはpythonコードとして記録されるので、直接実行や編集することで、
再度同じ図を出力することや、より詳細に手を加えることが可能です。


# Download
**MAT_PLOT** フォルダーを`git clone https://github.com/fukunoshima/GUI_for_matplotlib`でダウンロードしてください。



# 環境設定
python3 において
- pyqt5 
- matplotlib
をimportする必要があります。

ターミナルで
`pip3 install pyqt5 matplotlib`
などで設定できます。

# 使い方

## 起動
- `cd ./MAT_PLOT`
- `python3 matplot2.py`

## 作図 & 保存
- **find**ボタンを押し、ファイルを選択
- x, y の項目に選択したファイルの何番目のデータ列をx値, y値に選ぶかを選択 (一番左はじから0,1,2,...の順)
- 各オプションを選択
- **Plot!** を押すと図が描かれる
- **save filenames** に保存したいファイル名を選択(defaultはplot.pdf, png等でも保存可能)
- **Save** ボタンを押すと図が保存されるとともに、`./MAT_PLOT/Log/` 内部に同じ図を再生するpythonコードが生成される(plot.pdfで保存した場合はplot-日付.py)。

## 各種オプション
- lw: 線幅
- label: lagend onにチェックがある場合に線の名前指定
- lc: 線色
- lt: 線種
- xlog, ylog: 対数グラフ
- Limit Scale on: x, y軸の範囲を指定
- Label on: x, y軸のラベルを設定
- Legend on: legendの配置および文字サイズを指定

## 過去の履歴を再現
- **log**ボタンを押すと`./MAT_PLOT/Log/`内部のpython ファイルを選択できる。
- **Plot!** を押すと過去の図が再現される(ただし現バージョンではこれ以上の編集ができない)

## オススメの使い方
コードを書くのが面倒なときや、一度pythonコードをこのコードを生成してからより詳細に作り込みたいときによく使用しています。
あと、pythonコード初学者の人に図の生成法を説明するさいなどに見本となるかもしれません。

