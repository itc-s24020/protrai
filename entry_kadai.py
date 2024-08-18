import tkinter as tk 

def dispLabel():

    a = entry.get()
    print(f"aは{type(a)}")
    lbl.config(text=f"{a}さんこんにちは")
    
root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200")

lbl = tk.Label(text="ラベル", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica",20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
