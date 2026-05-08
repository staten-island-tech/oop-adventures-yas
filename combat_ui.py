import random
import tkinter as tk
import monster
import hero

def combat_ui():
    combat=tk.Tk()
    combat.title("Battle Started!!")
    combat.geometry("1920x1280")
    combat.configure(bg = "red")

    bg = tk.PhotoImage(file="image.png")
    bg_label = tk.Label(combat, image=bg)
    bg_label.place(relheight=1, relwidth=1)

    player = tk.PhotoImage(file="combat_sprite.png")
    player_label = tk.Label(combat, image=player)
    player_label.place(relx=0.2, rely=0.45, anchor=tk.CENTER, width=500, height=500)

    combat.mainloop()
combat_ui()