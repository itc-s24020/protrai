import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    # 画像を読み込み、グレースケールに変換
    newImage = PIL.Image.open(path).convert("L")
    
    # 画像を90度回転
    newImage = newImage.rotate(90)
    
    # 画像を水平方向に反転
    newImage = newImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    
    # 画像サイズを300x300に調整
    newImage = newImage.resize((300, 300))
    
    # 画像データをPhotoImageオブジェクトに変換
    imageData = PIL.ImageTk.PhotoImage(newImage)
    
    # ラベルに画像を設定
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command=openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()

tk.mainloop()
