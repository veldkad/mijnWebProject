import tkinter as tk
import customtkinter as ctk
import sqlite3

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("1200x800")
root.title("Buienradardgui")

def query():
    conn = sqlite3.connect("dataweerstations.db")
    c = conn.cursor()
    c.execute("SELECT * FROM stationdata order by id desc")
    records = c.fetchmany(25)
        
    print_records = ''
    for record in records: 
        print_records += str(record) + "\n"

    query_label = ctk.CTkLabel(root,text=print_records,justify="left")
    query_label.grid(row=1,column=0, columnspan=4,ipadx=20,ipady=10)
    
    conn.commit()
    conn.close()




# label =  ctk.CTkLabel(root, text="weerdata",font=('Arial',18), text_color="grey")
# label.pack(padx=20,pady=40)
# textbox = ctk.CTkTextbox(root,height=3,font=('Arial',12))
# textbox.pack()

# buttonframe = ctk.CTkFrame(root)
# buttonframe.columnconfigure(0 , weight=1)
# buttonframe.columnconfigure(1 , weight=1)
# buttonframe.columnconfigure(2 , weight=1)

btn1 = ctk.CTkButton(root, text="Show records", font=('Arial',10),command=query)
btn1.grid(row=0,column=0,sticky=ctk.W+ctk.E)
text1 = ctk.CTkTextbox(root,width=400,height=10)
text1.grid(row=0,column=2)


# buttonframe.pack(fill="x")

root.mainloop()