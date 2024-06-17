#GUIで動くアプリ

import tkinter as tk #まずこの行を書く

root = tk.Tk()#初めのおまじない
root.geometry("300x200")#運動のサイズを決める
root.title("アプリの練習")
lbl = tk.Label(text="Hello World")
lbl.pack()#lblを配置


root.mainloop()#終わりのおまじない
