import tkinter as tk
import random
# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("800x600")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Hello LANH")
canvas = tk.Canvas(frame)
#Function :
#-------move_gun:
def move_gun_to_right(event):
    global my_gun
    if canvas.coords(my_gun)[0] < 750:
        canvas.move(my_gun, 20, 0)

def move_gun_to_left(event):
    global my_gun
    if canvas.coords(my_gun)[0] > 50:
        canvas.move(my_gun, -20, 0)
def move_gun_to_up(event):
    global my_gun
    if canvas.coords(my_gun)[1] < 600 and canvas.coords(my_gun)[1] > 60:
        canvas.move(my_gun,0,-10)
def move_gun_to_down(envet):
    global my_gun
    if canvas.coords(my_gun)[1] > 50 and canvas.coords(my_gun)[1] < 550:
        canvas.move(my_gun, 0, 10)
# enemy with function
enemy1 = tk.PhotoImage(file = "Image\enemy1.png")
my_enemy1 = canvas.create_image(150,50,image = enemy1)
x1 = 150
y1 = 0
def enemy1_run():
    global my_enemy1 ,x1, y1, my_gun
    # if canvas.coords(my_enemy1)[0] == canvas.coords(my_gun)[0] and canvas.coords(my_enemy1)[1] == canvas.coords(my_gun)[1]:
    #     canvas.delete("all")
    #     canvas.create_text(400, 300, text = "LOSE !")
    canvas.moveto(my_enemy1, x1, y1)
    x1 += 0
    y1 += 1
    if y1 < 600:
        canvas.after(10, lambda :enemy1_run())
    else:
        x1 = 150
        y1 = 0
        canvas.after(10, lambda :enemy1_run())
enemy2 = tk.PhotoImage(file = "Image\enemy2.png")
my_enemy2 = canvas.create_image(350, 50, image = enemy2)
x2 = 350
y2 = 0
def enemy2_run():
    global my_enemy2 , x2, y2, my_gun
    # if canvas.coords(my_enemy2)[0] == canvas.coords(my_gun)[0] and canvas.coords(my_enemy2)[1] == canvas.coords(my_gun)[1]:
    #     canvas.delete("all")
    #     canvas.create_text(400, 300, text="LOSE !")
    canvas.moveto(my_enemy2, x2, y2)
    x2 += 0
    y2 += 1
    if y2 < 600:
        canvas.after(50, lambda:enemy2_run())
    else:
        x2 = 350
        y2 = 0
        canvas.after(10, lambda:enemy2_run())
enemy3 = tk.PhotoImage(file = "Image\enemy3.png")
my_enemy3 = canvas.create_image(550, 50, image = enemy3)
x3 = 550
y3 = 0
def enemy3_run():
    global my_enemy3 , x3, y3, my_gun
    # if canvas.coords(my_enemy3)[0] == canvas.coords(my_gun)[0] and canvas.coords(my_enemy3)[1] == canvas.coords(my_gun)[1]:
    #     canvas.delete("all")
    #     canvas.create_text(400,300,text="LOSE !")
    canvas.moveto(my_enemy3, x3, y3)
    x3 += 0
    y3 += 1
    if y3 < 600:
        canvas.after(20, lambda: enemy3_run())
    else:
        x3 = 550
        y3 = 0
        canvas.after(10, lambda: enemy3_run())
#bullet




canvas.pack(expand=True, fill = 'both')

# --------Player:
image = tk.PhotoImage(file = "Image\gun.png")
my_gun = canvas.create_image(400, 550, image = image)
bullet = tk.PhotoImage(file = "Image\bullet.png")
canvas.create_text(720,10,fill="darkblue",text="Score:")

# Call enamy all
enemy1_run()
enemy2_run()
enemy3_run()
# pack means "draw what i put inside"
frame.pack(expand=True, fill = 'both')
root.resizable(False,False)
# canvas.create_text(600,700,fill)
#-----move-gun
root.bind("<Right>",move_gun_to_right)
root.bind("<Left>",move_gun_to_left)
root.bind("<Up>",move_gun_to_up)
root.bind("<Down>",move_gun_to_down)
# Display all
root.mainloop()