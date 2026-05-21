import random
import tkinter as tk
import monster
import slime_battle
import goblin_battle
from hero import hero
from PIL import Image, ImageTk

class combat_UI:
    def __init__(self, enemy_sprite, combat, attckb, inventory, run, max_hp, enemy_max_hp, fdmg, strike, slash, endmg, enemy, turn, hero, healthbarfgf, healthbarfg):
        self.enemy_sprite = enemy_sprite  
        self.combat = None  
        self.attckb = None
        self.inventory = None
        self.run = None
        self.max_hp = max_hp
        self.enemy_max_hp = enemy_max_hp
        self.fdmg = None
        self.strike = None
        self.slash = None
        self.endmg = None
        self.enemy = enemy
        self.turn = True
        self.hero = hero
        self.healthbarfgf = None
        self.healthbarfg = None
    def determine_enemy(self):
        if self.enemy.species == "slime":
            self.create_combat_ui("slime")
        if self.enemy.species == "skeleton":
            self.create_combat_ui("skeleton")
        if self.enemy.species == "witch":
            self.create_combat_ui("witch")
        if self.enemy.species == "goblin":
            self.create_combat_ui("goblin")
    def create_combat_ui(self, enemy_sprite):
        combat=tk.Tk()
        combat.title("Battle Started!!")
        combat.geometry("1920x1280")
        combat.configure(bg = "red")
        bg = Image.open("bg.png").convert("RGBA")
        sprite = Image.open("combat_sprite.png").convert("RGBA")
        enemy_sprite = Image.open(f"{enemy_sprite}.png").convert("RGBA")
        sprite = sprite.resize((500, 500), Image.LANCZOS)
        enemy_sprite = enemy_sprite.resize((500, 500), Image.LANCZOS)
        if self.enemy.species == "slime":
            enemy_sprite = enemy_sprite.transpose(Image.FLIP_LEFT_RIGHT)
        bg_w, bg_h = bg.size
        x = int(bg_w * 0.2) - sprite.width // 2
        y = int(bg_h * 0.45) - sprite.height // 2
        x1 = int(bg_w * 0.8) - enemy_sprite.width // 2
        y1 = int(bg_h * 0.45) - enemy_sprite.height // 2
        bg.paste(sprite, (x, y), sprite)
        bg.paste(enemy_sprite, (x1, y1), enemy_sprite)
        tk_img = ImageTk.PhotoImage(bg)
        bg_label = tk.Label(combat, image=tk_img)
        bg_label.image = tk_img 
        bg_label.place(relheight=1, relwidth=1)
        healthbarbg = tk.Label (combat, bg="gray")
        healthbarbg.place(relx=0.8, rely=0.1, anchor=tk.CENTER, width=300, height=50)
        healthbarbgf = tk.Label (combat, bg="gray")
        healthbarbgf.place(relx=0.2, rely=0.1, anchor=tk.CENTER, width=300, height=50)
        self.healthbarfg = tk.Label(combat, bg="red")
        self.healthbarfgf = tk.Label(combat, bg="red")
        self.healthbarfg.place(relx=0.8, rely=0.1, anchor=tk.CENTER, width=300, height=50)
        self.healthbarfgf.place(relx=0.2, rely=0.1, anchor=tk.CENTER, width=300, height=50)
        self.combat = combat
    def buttons(self):
        attackb = tk.Button(self.combat, text="Attack", font=("Arial", 75), command=self.attack_window, bg="red")
        attackb.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        inventory = tk.Button(self.combat, text="Inventory", font=("Arial", 75), command=lambda: print("Inventory"), bg="red")
        inventory.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        run = tk.Button(self.combat, text="Run", font=("Arial", 75), command=lambda: self.run_window(), bg="red")
        run.place(relx=0.8, rely=0.8, anchor=tk.CENTER, width=500, height=250)    
        self.attackb = attackb
        self.inventory = inventory
        self.run = run
    def attack_window(self):
        self.attackb.destroy()
        self.inventory.destroy()
        self.run.destroy()
        strike = tk.Button(self.combat, text="Basic Strike!!", font=("Arial", 60), command=self.hero_strike)
        strike.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        slash = tk.Button(self.combat, text="Weapon Attack!!", font=("Arial", 45), command= self.hero_weapon_attack)
        slash.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        self.strike = strike
        self.slash = slash
        self.combat.update_idletasks()
    def run_window(self):
        self.attackb.destroy()
        self.inventory.destroy()
        self.run.destroy()
        runw=tk.Label(self.combat, text="Theres no running you pu-coward", font=("Arial", 50), bg="purple")
        runw.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
        self.combat.update_idletasks()
        self.combat.after(1000, self.ene_turn)
        self.combat.after(1000, runw.destroy)
    def hero_strike(self):
        dmg = self.hero.attack(self.enemy, self.hero.strength)
        self.fdmg = tk.Label (self.combat, text=f"{dmg} damage!!", font=("Arial", 30), bg="purple")
        self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=300)
        self.healthbare()
        self.combat.after(1000,self.determine_dead)
    def healthbarf(self):
        self.healthbarfgf.destroy()
        hp = self.hero.health
        health_percentagef = hp / self.max_hp
        self.healthbarfgf = tk.Label(self.combat, bg="red")
        self.healthbarfgf.place(relx=0.2, rely=0.1, anchor=tk.CENTER, width=300 * health_percentagef, height=50)
    def healthbare(self):
        self.healthbarfg.destroy()
        enemy_hp = self.enemy.hp
        health_percentage = enemy_hp / self.enemy_max_hp
        self.healthbarfg = tk.Label(self.combat, bg="red")
        self.healthbarfg.place(relx=0.8, rely=0.1, anchor=tk.CENTER, width=300 * health_percentage, height=50)
    def determine_dead(self):
        if self.enemy.dead == True:
            defeat = tk.Label(self.combat, text=f"You defeated the {self.enemy.species}!!", font=("Arial", 50), bg="purple")
            defeat.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
            self.healthbarfg.destroy()
            self.combat.update_idletasks()
            self.combat.after(2000, self.combat.destroy)
        else:
            self.combat.update_idletasks()
            self.combat.after(1000, self.fdmg.destroy)
            self.combat.after(1000, self.strike.destroy)
            self.combat.after(1000, self.slash.destroy)
            self.combat.after(1000, self.ene_turn)
    def ene_turn(self):
        if self.enemy.species == "slime":
            edmg, psn = self.enemy.strike(self.hero)
            self.endmg = tk.Label (self.combat, text=f"you took {edmg} damage!! ({psn} poison damge)",wraplength= 250,  font=("Arial", 30), bg="purple")
        else:
            edmg = self.enemy.strike(self.hero)
            self.endmg = tk.Label (self.combat, text=f"you took {edmg} damage!!", font=("Arial", 30), bg="purple")
        self.endmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=300)
        self.healthbarf()
        self.combat.after(1000,self.determine_deadf)
    def determine_deadf(self):
        if self.hero.health <= 0:
            defeat = tk.Label(self.combat, text=f"You were defeated by the {self.enemy.species}!!", font=("Arial", 50), bg="purple")
            defeat.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
            self.combat.update_idletasks()
            self.combat.after(2000, self.combat.destroy)
        else: 
            self.combat.update_idletasks()
            self.combat.after(1000, self.endmg.destroy)
            self.turn = True
            self.combat.update_idletasks()
            self.combat_loop()
    def combat_loop(self):
        if self.turn == True:
            self.healthbarf()
            self.healthbare()
            self.buttons()
            self.turn = False
        else: 
            self.ene_turn()
            self.buttons()
    def hero_weapon_attack(self):
        dmg = self.hero.weapon_attack(self.enemy, self.hero.weapon)
        self.fdmg = tk.Label (self.combat, text=f"{dmg} damage!!", font=("Arial", 30), bg="purple")
        self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=300)
        self.healthbare()
        self.combat.after(1000,self.determine_dead)
    def fight(self):
        self.determine_enemy()
        self.healthbarf()
        self.healthbare()
        self.buttons()
        self.combat.mainloop()
    


d = hero(100, 100, 100, 10, None, 1, 0, 10, 0, 0, None, 10)
e = slime_battle.slime(3, 10, 1, False, 0)
a = combat_UI(None, None, None, None, None, d.health, e.hp, None, None, None, None, e, True, d, None, None)
a.fight()
 
