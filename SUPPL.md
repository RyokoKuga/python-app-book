# 補足情報  

本書の補足情報を掲載しております。  

## P.64: リスト 4.1.1： 設定ファイルの生成

ここでは、configparserモジュールに用意されているwrite()メソッドを使用しております(最終行の「config.write(file)」)。  

```python
# configparserのインポート
import configparser

# インスタンス化
config = configparser.ConfigParser()
# 設定ファイルの内容
config["Run1"] = {
    "app1": r"C:\WINDOWS\system32\notepad.exe",
    "app2": r"C:\Program Files\Internet Explorer\iexplore.exe"
}
# 設定ファイルへ書込み
with open("config.ini", "w+") as file:
    config.write(file)
```
インスタンス化した変数configのあとに「.」をつけてwrite()とコードを入力していることから、configparserモジュールのwrite()メソッドを使用していることを意味します(モジュール内のメソッドの呼び出し方法については、本書P20に記載)。  

一方、P51リスト3.3.3では、Python標準で用意されているファイルの書き込みを行うwrite()メソッドを使用しています。  

```python
# ファイルへ書き込み
with open("test.txt", "a+") as file:
    file.write("OK?")
```
メソッド名は同じですが、元となるモジュールが異なるので混乱しないように注意しましょう。  

configparserのwrite()メソッドの引数は、ファイルオブジェクト(ここでは、変数fileに代入した処理)である必要があります。一方、Python標準のファイルの書き込みを行うwrite()メソッドの引数は、文字列である必要があります。  

## P.178: リスト 6.1.15： x 軸方向のスクロールバー

x軸方向のスクロールバーを実際にテストしたい場合は、以下の箇所を変更してください。  

```python
# 変更前
txtbox = tk.Text(frame, width = 60, height = 20)
```
```python
# 変更後「wrap = "none"」の追加
txtbox = tk.Text(frame, width = 60, height = 20, wrap = "none")
```
Textウイジットのwrap = "none"オプションは、テキストボックス中の長い行の折り返しを無効にするためのものです。  
テキストボックスの幅以上の文字列を入力すると、x軸方向のスクロールバーが動作します。  
サンプルファイル([Chapter_6-1.ipynb](./Chapter_6/Chapter_6-1.ipynb))にも補足情報を追加しました。
</br>
</br>
### ★以下は、最新版(第2版)にて追記しましたが、つまずきやすい箇所なので特にご注意ください。
## P.30: リスト2.4.4： GUIへ関数の追加

tk.Button()の引数へ「command = run_func」を追加する際は、,(コンマ)で区切ることを忘れないようにしてください。
引数内の各引数間は、必ず,(コンマ)で区切る必要があります。  

```python
# Runボタン
run_button = tk.Button(root, text = "Run", command = run_func)
run_button.place(x = 110, y = 30)
```
,(コンマ)を忘れると、エラーが発生するので注意してください。 Python初心者がエラーを起こしがちな箇所です。  
</br>
</br>
## P.37他: リスト 3.1.1： メモ帳を起動するコード など

Windowsの場合、ファイルパスで用いている「円マーク」と「バックスラッシュ」は、使用しているフォントによって表示が変わります。表示は違いますが、プログラム上では同じ意味を持ちます。  
例えば、Arialなどの欧米フォントは「バックスラッシュ」、メイリオやMSゴシックなどの日本語フォントは「円マーク」になります。  

macOSの場合、「円マーク」と「バックスラッシュ」とは違う扱いになるので注意してください。ファイルパスは、「スラッシュ」で区切ってください。  

ファイルパス関連でエラーが発生する場合は、これら記号に誤りがないか特に注意して見返してみてください。  
