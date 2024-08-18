#dispImagekadai01
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path),convert("L")\
    .resize((32, 32)).resize((300,300))
    
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData


    
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

lbl = tk.Label(text="画像表示アプリバージョン2.0", font=("Helvetica", 20))

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()

lbl.pack()
btn.pack()
imageLabel.pack()



tk.mainloop()
