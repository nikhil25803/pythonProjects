import tkinter as tk
from typing import Text


window = tk.Tk()


window.geometry("400x210")
window.title("Billing Programme")


label = tk.Label(text="Enter Bill Total: ")
label.place(x=10,y=20,height=25)
label.config(bg="Lightgreen", padx=40)


entry_box = tk.Entry(text = "")
entry_box.place(x=10,y=40, width=110, height=25)

tk.mainloop()
