import tkinter as tk

root = tk.tk()
root.geometry("200×100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH")

lbl.pack()
btn.pack()
tk.mainloop()