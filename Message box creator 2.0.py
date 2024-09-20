import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

#ui
options = ["Box Type" ,"Error", "Info", "Warning", "Question"]

window = tk.Tk()

window.title("Message box creator 1.0")

random_var = tk.StringVar(value=options[0])


window.geometry('300x200')

window.resizable(0,0)

def show():
    titlemsg = texttitlee.get()
    descmsg = textDESC.get()
    optionC = random_var.get()
    print(f"Box is: {optionC}")

    if optionC == "Box Type":
        print("Cannot show box. Reason: Not a valid choise")
    elif optionC == "Error":
        messagebox.showerror(titlemsg, descmsg)
    elif optionC == "Info":
        messagebox.showinfo(titlemsg, descmsg)
    elif optionC == "Warning":
        messagebox.showwarning(titlemsg, descmsg)
    elif optionC == "Question":
        questionMSG = messagebox.askquestion(titlemsg, descmsg)
        if questionMSG == "yes":
            print("clicked yes")
        else:
            print("clicked no")

label1 = ttk.Label(master=window, text="Message box creator 1.0")
choiseBOX = ttk.OptionMenu(window, random_var, random_var.get(), *options)
buttonResault = ttk.Button(master=window, text="Show box", command=show)
textTitle = ttk.Label(master=window, text="Box Title")
textdescc = ttk.Label(master=window, text="Box Desc")
textDESC = ttk.Entry(master=window, width=30)
texttitlee = ttk.Entry(master=window, width=30)

label1.pack(pady=5)
textTitle.pack()
texttitlee.pack(pady=5)
textdescc.pack()
textDESC.pack(pady=5)
choiseBOX.pack()
buttonResault.pack(pady=5)




window.mainloop()