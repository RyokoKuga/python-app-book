# 補足情報  

本書の補足情報を掲載しております。  

## P.178: リスト 6.1.15： x 軸方向のスクロールバー

x軸方向のスクロールバーを実際にテストしたい場合は、以下の箇所を変更してください。  

```python
# 変更前
txtbox = tk.Text(frame, width = 60, height = 20)

# 変更後「wrap = "none"」の追加
txtbox = tk.Text(frame, width = 60, height = 20, wrap = "none")
```
Textウイジットのwrap = "none"オプションは、テキストボックス中の長い行の折り返しを無効にするためのものです。  
テキストボックスの幅以上の文字列を入力すると、x軸方向のスクロールバーが動作します。  
21'05/10付で、サンプルファイル([Chapter_6-1.ipynb](./Chapter_6/Chapter_6-1.ipynb))にも補足情報を追加しました。
