main_canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="thistle")
main_canvas.pack(pady=50)


### MOVING CANVAS OBJECTS ###
moving_oval = main_canvas.create_oval(x, y, x + 20, y + 20, fill="beige")

def move_left(event):
    x = -10 
    y = 0 
    main_canvas.move(moving_oval, x, y) # Function that moves shape object

def move_right(event):
    x = 10 
    y = 0 
    main_canvas.move(moving_oval, x, y) # Function that moves shape object

def move_up(event):
    x = 0 
    y = -10 
    main_canvas.move(moving_oval, x, y) # Function that moves shape object

def move_down(event):
    x = 0 
    y = 10 
    main_canvas.move(moving_oval, x, y) # Function that moves shape object


def pressing(event):
    if event.char == "p" : 
        main_canvas.itemconfig(moving_oval, fill="pink")
    
    if event.char == "b" : 
        main_canvas.itemconfig(moving_oval, fill="cornflower blue")
   
    if event.char == "c" : 
        main_canvas.itemconfig(moving_oval, fill="beige")
 
## EVENTS & BINDS IN TKINTER ##
# mainloop() keeps the window open while also updating the program
# i.e. it runs a event loop that "listens" for events

# Binds defined functions to arrow keys
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)


# <Key> works for any letter char
# Just be sure to identify it in the function
root.bind("<Key>", pressing)
root.mainloop()
