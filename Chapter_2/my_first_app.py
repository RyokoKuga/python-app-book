# coding: utf-8

# tkinterのインポート
import tkinter as tk

### 関数 ###
# 関数の定義
def runFunc():
    print("Hello!!")
    print("OK")

### GUI ###
# ウインドウの作成
root = tk.Tk()
# ウインドウのサイズ指定
root.geometry("250x100")

# Runボタン
run_button = tk.Button(root, text = "Run", command = runFunc)
run_button.place(x = 110, y = 30)

# ウインドウ状態の維持
root.mainloop()