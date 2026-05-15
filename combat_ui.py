import random
import tkinter as tk
import monster
import slime_battle
import goblin_battle
from hero import hero
from PIL import Image, ImageTk
import time

def determine_enemy(enemy):
    def create_combat_ui(enemy_sprite):
        enemy_max_hp = enemy.hp
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
        if enemy.species == "slime":
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
            def healthbar(enemy_max_hp):
                enemy_hp = enemy.hp
                health_percentage = enemy_hp / enemy_max_hp
                return health_percentage
            healthbarbg = tk.Label (combat, bg="gray")
            healthbarbg.place(relx=0.8, rely=0.1, anchor=tk.CENTER, width=300, height=50)
            healthbarfg = tk.Label(combat, bg="red")
            healthbarfg.place(relx=0.8, rely=0.1, anchor=tk.CENTER, width=300 * healthbar(enemy_max_hp), height=50)


            healthbar(enemy_max_hp)
            def attack_window():
                attackb.destroy()
                inventory.destroy()
                run.destroy()
                def hero_strike():
                    d.attack(enemy, d.strength)
                    if enemy.dead == True:
                        defeat = tk.Label(combat, text=f"You defeated the {enemy.species}!!", font=("Arial", 50), bg="purple")
                        defeat.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
                        healthbarfg.destroy()
                        combat.update_idletasks()
                        combat.after(2000, combat.destroy)
                    else:
                        strike.destroy()
                        slash.destroy()
                        buttons()
                strike = tk.Button(combat, text="Basic Strike!!", font=("Arial", 60), command=hero_strike)
                strike.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
                slash = tk.Button(combat, text="Weapon Attack!!", font=("Arial", 45), command=lambda: d.weapon_attack(enemy, d.strength, 0))
                slash.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
            attackb = tk.Button(combat, text="Attack", font=("Arial", 75), command=attack_window, bg="red")
            attackb.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
            inventory = tk.Button(combat, text="Inventory", font=("Arial", 75), command=lambda: print("Inventory"), bg="red")
            inventory.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
            run = tk.Button(combat, text="Run", font=("Arial", 75), command=lambda: print("Run"), bg="red")
            run.place(relx=0.8, rely=0.8, anchor=tk.CENTER, width=500, height=250)


        buttons()
        combat.mainloop()
            
    if enemy.species == "slime":
        create_combat_ui("slime")
    if enemy.species == "skeleton":
        create_combat_ui("skeleton")
    if enemy.species == "witch":
        create_combat_ui("witch")
    if enemy.species == "goblin":
        create_combat_ui("goblin")
d = hero(100, 100, 100, 10, None, 1, 0, 10, 0, 0, None)
determine_enemy(slime_battle.slime(3, 20, 1, False))
