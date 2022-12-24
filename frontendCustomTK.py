import tkinter as tk
import customtkinter as ctk


root = tk.Tk()
root.geometry("400x400")
root.title("Buienradardgui")
label =  tk.Label(root, text="weerdata",font=('Arial',18),bg='#3d6466',fg="white")
label.pack(padx=20,pady=40)
textbox = tk.Text(root,height=3,font=('Arial',12))
textbox.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0 , weight=1)
buttonframe.columnconfigure(1 , weight=1)
buttonframe.columnconfigure(2 , weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial',10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial',10))
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial',10))
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial',10))
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial',10))
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial',10))
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

buttonframe.pack(fill="x")

root.mainloop()