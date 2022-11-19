from tkinter import*
from tkinter import ttk
from tkinter.ttk import *

root = Tk()
root.geometry("600x400")
root.title("Checkbutton Practice")

flavours = ["chocolate", "vanilla", "strawberry"]

def show_chck_value():
        print(chck_var.get)

style = ttk.Style()
style.map("TCheckbutton",
        foreground=[('selected', 'red'), ('alternate', 'green')], statespec='!active'
          )


for flavour in flavours:
        chck_var = StringVar()
        chck_btn.set(0)
        chck_btn = ttk.Checkbutton(root, text=flavour, onvalue="hi", offvalue="bye", command=show_chck_value)
        chck_btn.grid(sticky="W", padx=(50, 0))
        chck_btn.config(state="!on")
        print(chck_btn.state())        # check the current state of a Checkbutton



root.mainloop()

# State Flags
# used to change the appearance of a widget during execution
# every ttk widget has a set of state flags
# each state is independent from other states & may be set (i.e. turned on) or reset (i.e. turned off)
# focus, pressed, selected, invalid
