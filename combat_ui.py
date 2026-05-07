import random
import tkinter as tk
import monster
import hero

def combat_ui():
    combat=tk.Tk()
    combat.title("Battle Started!!")
    combat.geometry("1920x1080")
    combat.configure(bg = "red")
    bg = tk.PhotoImage(file="image.png")
    bg_label = tk.Label(combat, image=bg)
    bg_label.place(x=0, y=0, width=1920, height=1080)
    combat.mainloop()
combat_ui()