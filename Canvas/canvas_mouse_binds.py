from tkinter import *


# VARIABLE CONSTANTS
WIDTH = 600
HEIGHT = 400 
x = WIDTH // 2
y = HEIGHT // 2


# Screen SetUp
root = Tk()
root.title("Move Objects within Canvas")
root.geometry("600x450")


# Canvas Setup
main_canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="thistle")
main_canvas.pack()
img = PhotoImage(file="poodle.png") 


### DRAGGING CANVAS OBJECTS ###
my_img = main_canvas.create_image(313, 196, image=img)
my_oval = main_canvas.create_oval(210, 320, 230, 340, fill="khaki") 


def drag(event):
    # "event.x" retrieves the current x-coor when mouse it clicked
    # "event.y" retrieves the current y-coor when mouse it clicked
    
    global img # addresses garbage collector glitch in tkinter 
    img = PhotoImage(file="poodle.png") 
    my_img = main_canvas.create_image(event.x, event.y, image=img)
    # my_oval = main_canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="khaki") 

    current_coor.config(text="x-coor: " + str(event.x) +"\ny-coor:" + str(event.y))


# def drag(event):
#     # event.x
#     # event.y
#     current_coor.config(text="x-coor: " + str(event.x) +"\ny-coor:" + str(event.y))

current_coor = Label(root, text="")
current_coor.pack()

# "B1-Motion" means the button of your mouse is clicked
main_canvas.bind("<B1-Motion>", drag)


root.mainloop()
