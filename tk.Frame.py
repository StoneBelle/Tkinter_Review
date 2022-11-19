# Import Tkinter Library
from tkinter import *

# Create an instance of Tkinter frame
wn= Tk()

# Set the size of the application window
wn.geometry("700x350")

# Create a class to define the frame
class NewFrame(Frame):
   def __init__(self, wn):
      super().__init__()
      self["height"] = 200
      self["width"] = 200
      self["bd"] = 10
      self["relief"] = RAISED
      self["bg"] = "#aa11bb"

# Create Frame object
frame_a= NewFrame(wn)
frame_b= NewFrame(wn)
frame_a.grid(row=0, column=0)
frame_b.grid(row=0, column=1)

win.mainloop()
