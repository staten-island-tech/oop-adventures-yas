import random
import tkinter as tk
import monster
import slime_battle
import hero
from PIL import Image, ImageTk

def determine_enemy(enemy):
    def create_combat_ui(enemy_sprite):
        combat=tk.Tk()
        combat.title("Battle Started!!")
        combat.geometry("1920x1280")
        combat.configure(bg = "red")
                # load background and sprite as RGBA so alpha is preserved
        bg = Image.open("bg.png").convert("RGBA")
        sprite = Image.open("combat_sprite.png").convert("RGBA")
        enemy_sprite = Image.open(f"{enemy_sprite}.png").convert("RGBA")
                # optional: resize sprite to desired size
        sprite = sprite.resize((500, 500), Image.LANCZOS)
        enemy_sprite = enemy_sprite.resize((500, 500), Image.LANCZOS)
        enemy_sprite = enemy_sprite.transpose(Image.FLIP_LEFT_RIGHT)

                # compute paste position (center at relx=0.2, rely=0.45)
        bg_w, bg_h = bg.size
        x = int(bg_w * 0.2) - sprite.width // 2
        y = int(bg_h * 0.45) - sprite.height // 2
        x1 = int(bg_w * 0.8) - enemy_sprite.width // 2
        y1 = int(bg_h * 0.45) - enemy_sprite.height // 2

                # paste sprite onto background using its alpha channel as the mask
        bg.paste(sprite, (x, y), sprite)
        bg.paste(enemy_sprite, (x1, y1), enemy_sprite)
                # convert the composed image for Tkinter
        tk_img = ImageTk.PhotoImage(bg)
        bg_label = tk.Label(combat, image=tk_img)
        bg_label.image = tk_img 
        bg_label.place(relheight=1, relwidth=1)

        def buttons():
            def attack_window():
                attack.destroy()
                inventory.destroy()
                run.destroy()
                strike = tk.Button(combat, text="Basic Strike!!", font=("Arial", 60), command=lambda: hero.attack(enemy, hero.strength))
                strike.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
                slash = tk.Button(combat, text="Weapon Attack!!", font=("Arial", 45), command=lambda: hero.weapon_attack(enemy, hero.strength, 0))
                slash.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
            attack = tk.Button(combat, text="Attack", font=("Arial", 75), command=attack_window, bg="red")
            attack.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
            inventory = tk.Button(combat, text="Inventory", font=("Arial", 75), command=lambda: print("Inventory"), bg="red")
            inventory.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
            run = tk.Button(combat, text="Run", font=("Arial", 75), command=lambda: print("Run"), bg="red")
            run.place(relx=0.8, rely=0.8, anchor=tk.CENTER, width=500, height=250)
            
        buttons()
        combat.mainloop()
            
    if enemy["species"] == "slime":
        create_combat_ui("slime")
    if enemy["species"] == "skeleton":
        create_combat_ui("skeleton")
    if enemy["species"] == "witch":
        create_combat_ui("witch")
    if enemy["species"] == "goblin":
        create_combat_ui("goblin")

determine_enemy(slime_battle)
