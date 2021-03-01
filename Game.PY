import tkinter as tk
import random

# FUNCTION ---------------------------------------------------------------------------

def move_gun_to_right(event):
    if canvas.coords(my_gun)[0] < 750:
        canvas.move(my_gun, 20, 0)

def move_gun_to_left(event):
    if canvas.coords(my_gun)[0] > 50:
        canvas.move(my_gun, -20, 0)

def move_gun_to_up(event):
    if canvas.coords(my_gun)[1] < 600 and canvas.coords(my_gun)[1] > 60:
        canvas.move(my_gun,0,-10)
def move_gun_to_down(event):
    if canvas.coords(my_gun)[1] > 50 and canvas.coords(my_gun)[1] < 550:
        canvas.move(my_gun, 0, 10)
# Move enemies---------------------------------------------------------------------------------------------------------------------------------------
x1 = 150
y1 = 50
def enemyI():
    global x1 , y1
    x1 += 0 
    y1 += 1
    canvas.move(my_enemy1, 0, 10)
    canvas.after(10, enemyI)
x2 = 350
y2 = 50
def enemyII():
    global x2 , y2
    x2 += 0
    y2 += 1
    canvas.move(my_enemy2, 0, 10)
    canvas.after(20, enemyII)
x3 = 550
y3 = 50
def enemyIII():
    global x3, y3
    x3 += 0
    y3 += 1
    canvas.move(my_enemy3, 0, 10)
    canvas.after(20, enemyIII)
# GRAPHICS -----------------------------------------------------------------------


root = tk.Tk() 
root.geometry("800x600")
canvas = tk.Canvas(root)


# CREATE IMAGES-------------------------------------------------------------------
enemy1 = tk.PhotoImage(file = "Image\enemy1.png")
enemy2 = tk.PhotoImage(file = "Image\enemy2.png")
enemy3 = tk.PhotoImage(file = "Image\enemy3.png")
gun = tk.PhotoImage(file = "Image\gun.png")
bullet = tk.PhotoImage(file = "Image\\bullet.png")

my_enemy1 = canvas.create_image(150,50,image = enemy1)
my_enemy2 = canvas.create_image(350, 50, image = enemy2)
my_enemy3 = canvas.create_image(550, 50, image = enemy3)
my_gun = canvas.create_image(400, 550, image = gun)
shoot = canvas.create_image(400, 500, image = bullet)
score = canvas.create_text(720,10,fill="darkblue",text="Score:")

# Call enemy all
enemyI()
enemyII()
enemyIII()

root.bind("<Right>",move_gun_to_right)
root.bind("<Left>",move_gun_to_left)
root.bind("<Up>",move_gun_to_up)
root.bind("<Down>",move_gun_to_down)

canvas.pack(expand=True, fill = 'both')
root.mainloop()