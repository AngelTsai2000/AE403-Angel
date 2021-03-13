# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import tkinter.messagebox

def ClickMe():
    tkinter.messagebox.showinfo(title="提示", message="好痛")
 
window = tk.Tk()
 
window.title("我的第一個GUI程式")
 
window.geometry('300x300')
 
#label = tk.Label(window, text="我的GUI")
label = tk.Label(window, text="我的GUI", bg="#000", fg="#fff", width=20)
label.pack()
 
entry = tk.Entry(window, width=20)
entry.pack()
 
#button = tk.Button(window, text="按鈕")
button = tk.Button(window, text="按鈕", command=ClickMe)
button.pack()
 
window.mainloop()
