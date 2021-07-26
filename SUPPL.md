# 補足情報  

本書の補足情報を掲載しております。  

## P.30: リスト2.4.4： GUIへ関数の追加

tk.Button()の引数へ「command = run_func」を追加する際は、「**,(コンマ)**」で区切ることを忘れないようにしてください。
本書中では説明が不十分でしたが、引数内の各引数間は、必ず,(コンマ)で区切る必要があります。  

```python
# Runボタン
run_button = tk.Button(root, text = "Run", command = run_func)
run_button.place(x = 110, y = 30)
```
,(コンマ)を忘れると、エラーが発生するので注意してください。 Python初心者がエラーを起こしがちな箇所です。  
サンプルファイル([Chapter_2.ipynb](./Chapter_2/Chapter_2.ipynb))にも補足情報を追加しました。
</br>
</br>
## P.72: 図4-5. row, column による配置

図4-5の説明が分かりづらかったので補足します。grid()メソッドのrowとcolumnによる指定は、以下のように表にするとイメージしやすくなります。例えば、図4-5の左図では以下のような配置になります。

|  | column=0 | column=1 |
| :-: | :-: | :-: |
| row=0 |    | RUN2 |
| row=1 | RUN1 |    |
```python
# ボタン
run_button1 = tk.Button(frame, text = "RUN1")
run_button1.grid(row=1, column=0, padx = 5)

run_button2 = tk.Button(frame, text = "RUN2")
run_button2.grid(row = 0, column = 1, padx = 5)
```

一方、図4-5の右図では以下のような配置になります。column=0の列に値が存在しない場合は、ウインドウ上には表示されません。

|  | column=0 | column=1 |
| :-: | :-: | :-: |
| row=0 |    | RUN2 |
| row=1 |    | RUN1 |
```python
# ボタン
run_button1 = tk.Button(frame, text = "RUN1")
run_button1.grid(row=1, column=1, padx = 5)

run_button2 = tk.Button(frame, text = "RUN2")
run_button2.grid(row = 0, column = 1, padx = 5)
```

つまり、以下のようにコードを変更しても、実際にアプリケーション上で表示されるボタンの配置は同じになります。

|  | column=0 | column=1 |
| :-: | :-: | :-: |
| row=0 | RUN2 |    |
| row=1 | RUN1 |    |
```python
# ボタン
run_button1 = tk.Button(frame, text = "RUN1")
run_button1.grid(row=1, column=0, padx = 5)

run_button2 = tk.Button(frame, text = "RUN2")
run_button2.grid(row = 0, column = 0, padx = 5)
```

grid()メソッドのrowとcolumnによる指定で迷った場合は、一度、表に描いてみるとよいでしょう。  
サンプルファイル([Chapter_4-2.ipynb](./Chapter_4/Chapter_4-2.ipynb))にも補足情報を追加しました。  
</br>
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
