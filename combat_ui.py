import random
import tkinter as tk
import monster
import hero
from PIL import Image, ImageTk
class combat_ui():
    def __init__(self):
        self.create_combat_ui()
    def create_combat_ui(self):
        combat=tk.Tk()
        combat.title("Battle Started!!")
        combat.geometry("1920x1280")
        combat.configure(bg = "red")

        # load background and sprite as RGBA so alpha is preserved
        bg = Image.open("image.png").convert("RGBA")
        sprite = Image.open("combat_sprite.png").convert("RGBA")
        

        # optional: resize sprite to desired size
        sprite = sprite.resize((500, 500), Image.LANCZOS)

        # compute paste position (center at relx=0.2, rely=0.45)
        bg_w, bg_h = bg.size
        x = int(bg_w * 0.2) - sprite.width // 2
        y = int(bg_h * 0.45) - sprite.height // 2

        # paste sprite onto background using its alpha channel as the mask
        bg.paste(sprite, (x, y), sprite)

        # convert the composed image for Tkinter
        tk_img = ImageTk.PhotoImage(bg)
        bg_label = tk.Label(combat, image=tk_img)
        bg_label.image = tk_img 
        bg_label.place(relheight=1, relwidth=1)

        return combat
    def determine_enemy(self, enemy):
        global enemy_sprite
        if enemy == "slime":
            enemy_sprite = Image.open("slime_sprite.png").convert("RGBA")
        if enemy == "skeleton":
            enemy_sprite = Image.open("skeleton_sprite.png").convert("RGBA")
        if enemy == "witch":
            enemy_sprite = Image.open("witch_sprite.png").convert("RGBA")
        if enemy == "goblin":
            enemy_sprite = Image.open("goblin_sprite.png").convert("RGBA")

combat_ui = combat_ui()
combat_ui.create_combat_ui()