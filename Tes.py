from tkinter import *
root = Tk()
canvas = Canvas(root)
root.title("LANH_CODE")
root.geometry("600x600")
canvas.pack(expand=True,fill="both")
image = PhotoImage(file="C:/Users/student/Desktop/VC-GAME/Image/enemy1.png")
my_image = canvas.create_image(600,500,image = image)
root.mainloop()