import tkinter as tk
from tkinter import *


### CANVAS INTRO ###
# Canvas is a Tkinter widget 
# it creates a rectangular area inside the given window
# in that area you can add images, create shapes, and animate objects

# Screen Setup
root = tk.Tk()
root.title("Canvas Intro")
root.geometry("800x800")
root.configure(background="slate gray")

# Canavs Setup
main_canvas = Canvas(root, width=300, height=200)
main_canvas.pack(pady=100)

sec_canvas = Canvas(root, width=400, height=300)
sec_canvas.pack(pady=100)

### DRAWING SHAPES ON CANVAS ###
# Canvas uses a coordiante system 
# (0, 0) being at the top left corner
# Provide the (x1, y1) and (x2 & y2) coors when making a shape
# Depending on the shape the coors refer to different things
# regardless, Tkinter will connect the dots



# Create a Line
# Starting Point: (x1, y1)
# Ending Point: (x2, y2)
# main_canvas.create_line(x1, y1, x2, y2, fill="color")
# dash=(dash px size, space size)

hori_line = main_canvas.create_line(0,  100, 300, 100, fill="red")
verti_line =main_canvas.create_line(150, 200, 150, 0, fill="red", dash=(4,1)) 

# Create a Rectangle / Sqaure
# Top Left: (x1, y1)
# Bottom Right: (x2, y2)
# main_canvas.create_rectangle()

my_rect = main_canvas.create_rectangle(50, 50, 250, 150)
my_sqr = main_canvas.create_rectangle(130, 80, 170, 120, fill="green")


# Create Oval
# Top Left: (x1, y1)
# Bottom Right: (x2, y2)
# Similar to creating a rectangle except the oval goes inside the defined coors
my_oval = main_canvas.create_oval(130, 80, 170, 120, fill="beige")


### ADDITIONAL CANVAS NOTES ##
# Canvas places items in a stack
# this means new items are drawn on top of items already on the canvas
# items added to the canavs will remain there unless removed
# coords(), itemconfig(), or move() to modify a drawing
# delete() to remove an item


#Returns coordinates of specified shape
print("Coordinates of the object are:", main_canvas.coords(my_rect))

# changes colour of specified shape
main_canvas.itemconfig(my_sqr, fill="pink")

# Delete specific item/clear canvas
# main_canvas.delete(my_sqr)
# main_canvas.delete(ALL)


# Add an Image
img = PhotoImage(file="poodle.png") # Defines desired photo into a Canvas Photo Image

# Need to pass in (x, y) coors, anchor, and photo image
my_img = sec_canvas.create_image(170, 70, anchor="nw", image=img)
my_img_2 = sec_canvas.create_image(0, 0, anchor="nw", image=img)




root.mainloop()


