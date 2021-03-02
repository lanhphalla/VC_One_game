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
    if canvas.coords(my_gun)[1] < 560 and canvas.coords(my_gun)[1] > 50:
        canvas.move(my_gun,0,-20)
def move_gun_to_down(event):
    if canvas.coords(my_gun)[1] < 50 and canvas.coords(my_gun)[1] > 550:
        canvas.move(my_gun, 0, 20)
def bullet_player():
    global x_gun, y_gun, shoot,enemies
    canvas.moveto(shoot,x_gun,y_gun)
    x_gun += 0
    y_gun += -20
    if y_gun > 0:
        canvas.after(10, lambda: bullet_player())
    else:
        x_gun = canvas.coords(my_gun)[0]-25
        y_gun = canvas.coords(my_gun)[1]
        canvas.after(10, lambda: bullet_player())
# gun enemies 1---------------------------------------------------------------------------------------------------------------------------
def bullet_enemies1():
    global my_gun_enemy1, x_enemies1_gun, y_enemies1_gun, enemies
    canvas.moveto(my_gun_enemy1, x_enemies1_gun, y_enemies1_gun)
    x_enemies1_gun += 0
    y_enemies1_gun += 3
    if y_enemies1_gun < 550:
        canvas.after(10, lambda: bullet_enemies1())
    else:
        x_enemies1_gun = canvas.coords(my_enemy1)[0] -15
        y_enemies1_gun = canvas.coords(my_enemy1)[1]
        canvas.after(10, lambda: bullet_enemies1())
def bullet_enemies2():
    global my_gun_enemy2, x_enemies2_gun, y_enemies2_gun, enemies
    canvas.moveto(my_gun_enemy2, x_enemies2_gun, y_enemies2_gun)
    x_enemies2_gun += 0
    y_enemies2_gun += 3
    if y_enemies2_gun < 550:
        canvas.after(10, lambda: bullet_enemies2())
    else:
        x_enemies2_gun = canvas.coords(my_enemy2)[0] -15
        y_enemies2_gun = canvas.coords(my_enemy2)[1]
        canvas.after(10, lambda: bullet_enemies2())
def bullet_enemies3():
    global my_gun_enemy3, x_enemies3_gun, y_enemies3_gun, enemies
    canvas.moveto(my_gun_enemy3, x_enemies3_gun, y_enemies3_gun)
    x_enemies3_gun += 0
    y_enemies3_gun += 3
    if y_enemies3_gun < 550:
        canvas.after(10, lambda: bullet_enemies3())
    else:
        x_enemies3_gun = canvas.coords(my_enemy3)[0] -15
        y_enemies3_gun = canvas.coords(my_enemy3)[1]
        canvas.after(10, lambda: bullet_enemies3())
# Move enemies---------------------------------------------------------------------------------------------------------------------------------------
def move_enemies():
    global enemies
    for index in range(len(enemies)):
        position=canvas.coords(enemies[index][0])
        y_monster=position[1]
        x_monster=position[0]
        if x_monster>710:
            x_monster=300
        if y_monster>=605:
            canvas.moveto(enemies[index][0],x_monster,0)
        canvas.move(enemies[index][0],enemies[index][1],enemies[index][2])
    canvas.after(100,move_enemies)
    # delete enemies -----------------------------------------------------------------------------------------------------------------------------------
# def delete_enemies():
#     global enemies, shoot
#     for i in range(len(enemies)):
#         if canvas.coords(shoot)[1] == canvas.coords(enemies)[1]:
#             canvas.delete(enemies[i])
# GRAPHICS -----------------------------------------------------------------------
root = tk.Tk()
root.geometry("800x600")
canvas = tk.Canvas(root)
# CREATE IMAGES-------------------------------------------------------------------
enemy = tk.PhotoImage(file = "Image/enemy.png")
gun = tk.PhotoImage(file = "Image/gun.png")
bullet = tk.PhotoImage(file = "Image/bullet.png")
game_Background = tk.PhotoImage(file = "Image/bg.png")
bullet_enemy1 = tk.PhotoImage(file = "Image/bullet1.png")
bullet_enemy2 = tk.PhotoImage(file = "Image/bullet2.png")
bullet_enemy3 = tk.PhotoImage(file = "Image/bullet3.png")
game_background = canvas.create_image(400,300,image = game_Background)

my_enemy1 = canvas.create_image(150,0,image = enemy)
my_enemy2 = canvas.create_image(350, 0, image = enemy)
my_enemy3 = canvas.create_image(550, 0, image = enemy)
enemies = [[my_enemy1,0,6],[my_enemy2,0,9], [my_enemy3,0,12]]

shoot = canvas.create_image(400, 550, image = bullet)
my_gun = canvas.create_image(400, 550, image = gun)
my_gun_enemy1 = canvas.create_image(50, 50, image = bullet_enemy1)
my_gun_enemy2 = canvas.create_image(50, 50, image = bullet_enemy2)
my_gun_enemy3 = canvas. create_image(50, 50, image = bullet_enemy3)

x_gun = canvas.coords(my_gun)[0] - 25
y_gun = canvas.coords(my_gun)[1]  
x_enemies1_gun = canvas.coords(my_enemy1)[0]-15
y_enemies1_gun = canvas.coords(my_enemy1)[1]
x_enemies2_gun = canvas.coords(my_enemy2)[0]
y_enemies2_gun = canvas.coords(my_enemy2)[1]
x_enemies3_gun = canvas.coords(my_enemy3)[0]
y_enemies3_gun = canvas.coords(my_enemy3)[1]
# Call enemy all
move_enemies()
bullet_player()
bullet_enemies1()
bullet_enemies2()
bullet_enemies3()
# delete_enemies()
root.bind("<Right>",move_gun_to_right)
root.bind("<Left>",move_gun_to_left)
root.bind("<Up>",move_gun_to_up)
root.bind("<Down>",move_gun_to_down)
# root.bind("<k>", shoot_bullet)
canvas.pack(expand=True, fill = 'both')
root.resizable(False, False)
root.mainloop()