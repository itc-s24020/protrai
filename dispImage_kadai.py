#s24020

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

# ラベル「🎨画像表示アプリ バージョン2.0🎨」を最上部に追加
titleLabel = tk.Label(root, text="🎨画像表示アプリ バージョン2.0🎨", font=("Arial", 14), pady=10)
titleLabel.pack()

# ボタンと画像表示ラベルを配置
btn = tk.Button(root, text="ファイルを開く", command=openFile)
btn.pack(pady=10)

imageLabel = tk.Label(root)
imageLabel.pack()

tk.mainloop()
