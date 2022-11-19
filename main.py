from tkinter import *


wn = Tk()
wn.title("Radiobutton Practice")
wn.geometry("500x500")

opt_var = StringVar()

opt1 = Radiobutton( text="Xiao", variable=opt_var, value="1", command=lambda :print(opt_var.get())).pack()
opt2 = Radiobutton( text="Kazuha", variable=opt_var, value="2", command=lambda :print(opt_var.get())).pack()

print(type(opt1))
wn.mainloop()