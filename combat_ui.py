import random
import tkinter as tk
import monster
import slime_battle
import goblin_battle
import skeleton_battle
import witch_battle
from hero import hero
from PIL import Image, ImageTk
import spell 

class combat_UI:
    def __init__(self, enemy_sprite, combat, attckb, inventory, run, max_hp, enemy_max_hp, fdmg, strike, slash, endmg, enemy, turn, hero, healthbarfgf, healthbarfg, spell_attack, potion_pouch, weapon_pouch, spell_wheel, weapon, active_strength):
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
        self.spell_attack = None
        self.potion_pouch = None
        self.weapon_pouch = None
        self.spell_wheel = None
        self.weapon = weapon
        self.active_strength = active_strength
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
        combat.geometry("1920x1080")
        combat.configure(bg = "red")
        bg = Image.open("combat.png").convert("RGBA")
        sprite = Image.open("combat_sprite.png").convert("RGBA")
        enemy_sprite = Image.open(f"{enemy_sprite}.png").convert("RGBA")
        sprite = sprite.resize((350, 350), Image.LANCZOS)
        enemy_sprite = enemy_sprite.resize((350, 350), Image.LANCZOS)
        if self.enemy.species == "slime":
            enemy_sprite = enemy_sprite.transpose(Image.FLIP_LEFT_RIGHT)
        bg_w, bg_h = bg.size
        x = int(bg_w * 0.2) - sprite.width // 3
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
        healthbarbg.place(relx=0.8, rely=0.2, anchor=tk.CENTER, width=300, height=50)
        healthbarbgf = tk.Label (combat, bg="gray")
        healthbarbgf.place(relx=0.23, rely=0.2, anchor=tk.CENTER, width=300, height=50)
        self.healthbarfg = tk.Label(combat, bg="red")
        self.healthbarfgf = tk.Label(combat, bg="red")
        self.healthbarfg.place(relx=0.8, rely=0.2, anchor=tk.CENTER, width=300, height=50)
        self.healthbarfgf.place(relx=0.23, rely=0.2, anchor=tk.CENTER, width=300, height=50)
        self.combat = combat
    def buttons(self):
        self.attackb = tk.Button(self.combat, text="Attack", font=("Arial", 75), command=self.attack_window, bg="red")
        self.attackb.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        self.inventory = tk.Button(self.combat, text="Inventory", font=("Arial", 75), command=self.inventory_window, bg="red")
        self.inventory.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        self.run = tk.Button(self.combat, text="Run", font=("Arial", 75), command=lambda: self.run_window(), bg="red")
        self.run.place(relx=0.8, rely=0.8, anchor=tk.CENTER, width=500, height=250)        
    def attack_window(self):
        self.attackb.destroy()
        self.inventory.destroy()
        self.run.destroy()
        self.strike = tk.Button(self.combat, text="Basic Strike!!", font=("Arial", 60 ), command=lambda: [self.strike.destroy(), self.slash.destroy(), self.spell_attack.destroy(), self.hero_strike()] )
        self.strike.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        self.slash = tk.Button(self.combat, text="Weapon Attack!!", font=("Arial", 45), command=lambda: [self.strike.destroy(), self.slash.destroy(), self.spell_attack.destroy(), self.hero_weapon_attack()])
        self.slash.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        self.spell_attack = tk.Button(self.combat, text="Spell Attack!!", font=("Arial", 45), command=lambda: [self.strike.destroy(), self.slash.destroy(), self.spell_attack.destroy(), self.hero_spell_attack()])
        self.spell_attack.place(relx=0.8, rely=0.8, anchor=tk.CENTER, width=500, height=250)
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
    def inventory_window(self):
        self.attackb.destroy()
        self.inventory.destroy()
        self.run.destroy()
        self.weapon_pouch = tk.Button(self.combat, text="Weapons", font=("Arial", 60), command=self.weapon_window)
        self.weapon_pouch.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        self.potion_pouch = tk.Button(self.combat, text="Potions", font=("Arial", 60), command=self.potion_window)
        self.potion_pouch.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        self.spell_wheel = tk.Button(self.combat, text="Spells", font=("Arial", 60), command=self.spell_window)
        self.spell_wheel.place(relx=0.8, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        self.combat.update_idletasks()
    def potion_window(self):
        self.weapon_pouch.destroy()
        self.potion_pouch.destroy()
        self.spell_wheel.destroy()
        potion1 = tk.Button(self.combat, text=f"Type:{self.hero.inventory['Potions'][0]['name']}, Count: {self.hero.inventory['Potions'][0]['count']}" , font=("Arial", 20), command=lambda: [ potion1.destroy(), potion2.destroy(), potion3.destroy(), self.health_potion()])
        potion1.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        potion2 = tk.Button(self.combat, text=f"Type:{self.hero.inventory['Potions'][1]['name']}, Count: {self.hero.inventory['Potions'][1]['count']}" , font=("Arial", 20), command=lambda:  [potion1.destroy(), potion2.destroy(), potion3.destroy(), self.strength_potion()])
        potion2.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        potion3 = tk.Button(self.combat, text=f"Type:{self.hero.inventory['Potions'][2]['name']}, Count: {self.hero.inventory['Potions'][2]['count']}" , font=("Arial", 20), command=lambda: [ potion1.destroy(), potion2.destroy(), potion3.destroy(), self.mana_potion()])
        potion3.place(relx=0.8, rely=0.8, anchor=tk.CENTER, width=500, height=250)
    def strength_potion(self):
        if self.hero.inventory["Potions"][1]["count"] > 0:
            strength_potion = tk.Label(self.combat, text=f"You used a {self.hero.inventory['Potions'][1]['name']}!! and gained {self.hero.inventory['Potions'][1]['strong']} strength for this battle", font=("Arial", 20), bg="purple")
            strength_potion.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)

            self.active_strength += self.hero.inventory["Potions"][1]["strong"]
            self.hero.inventory["Potions"][1]["count"] -= 1
            self.combat.update_idletasks()
            self.combat.after(1000, strength_potion.destroy)
            self.combat.after(1000, self.ene_turn)
        else:
            no_potions = tk.Label(self.combat, text="You have no strength potions left!!", font=("Arial", 30), bg="purple")
            no_potions.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
            self.combat.update_idletasks()
            self.combat.after(1000, no_potions.destroy)
            self.combat.after(1000, self.buttons)
    def health_potion(self):
        if self.hero.inventory["Potions"][0]["count"] > 0:
            health_potion = tk.Label(self.combat, text=f"You used a {self.hero.inventory['Potions'][0]['name']}!! and healed {self.hero.inventory['Potions'][0]['heal']}", font=("Arial", 30), bg="purple")
            health_potion.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)

            self.hero.health += self.hero.inventory["Potions"][0]["heal"]
            self.hero.inventory["Potions"][0]["count"] -= 1
            if self.hero.health > self.max_hp:
                self.hero.health = self.max_hp
            self.healthbarf()
            self.combat.update_idletasks()
            self.combat.after(1000, health_potion.destroy)
            self.combat.after(1000, self.ene_turn)
        else:
            no_potions = tk.Label(self.combat, text="You have no health potions left!!", font=("Arial", 30), bg="purple")
            no_potions.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
            self.combat.update_idletasks()
            self.combat.after(1000, no_potions.destroy)
            self.combat.after(1000, self.buttons)
    def mana_potion(self):
        if self.hero.inventory["Potions"][2]["count"] > 0:
            mana_potion = tk.Label(self.combat, text=f"You used a {self.hero.inventory['Potions'][2]['name']}!! and restored {self.hero.inventory['Potions'][2]['mana']}", font=("Arial", 30), bg="purple")
            mana_potion.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)

            self.hero.mana += self.hero.inventory["Potions"][2]["mana"]
            self.hero.inventory["Potions"][2]["count"] -= 1
            if self.hero.health > self.max_hp:
                self.hero.health = self.max_hp
            self.healthbarf()
            self.combat.update_idletasks()
            self.combat.after(1000, mana_potion.destroy)
            self.combat.after(1000, self.ene_turn)
        else:
            no_potions = tk.Label(self.combat, text="You have no health potions left!!", font=("Arial", 30), bg="purple")
            no_potions.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
            self.combat.update_idletasks()
            self.combat.after(1000, no_potions.destroy)
            self.combat.after(1000, self.buttons)
    def spell_window(self):
        self.weapon_pouch.destroy()
        self.potion_pouch.destroy()
        self.spell_wheel.destroy()
        spell1 = tk.Button(self.combat, text=f"equip {self.hero.inventory['Spells'][0]['name']}", font=("Arial", 40), command=lambda: [self.select_spell_1(), spell1.destroy(), spell2.destroy(), spell3.destroy()])
        spell1.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        spell2 = tk.Button(self.combat, text=f"equip {self.hero.inventory['Spells'][1]['name']}", font=("Arial", 40), command=lambda: [self.select_spell_2(), spell1.destroy(), spell2.destroy(), spell3.destroy()])
        spell2.place(relx=0.8, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        spell3 = tk.Button(self.combat, text=f"equip {self.hero.inventory['Spells'][2]['name']}", font=("Arial", 40), command=lambda: [self.select_spell_3(), spell1.destroy(), spell2.destroy(), spell3.destroy()])
        spell3.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
    def select_spell_1(self):
        selected = tk.Label(self.combat, text=f"You equipped {self.hero.inventory['Spells'][0]['name']}!!", font=("Arial", 50), bg="purple")
        selected.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
        self.hero.equipped_spell = self.hero.inventory["Spells"][0]
        self.combat.update_idletasks()
        self.combat.after(1000, selected.destroy)
        self.combat.after(1000, self.buttons)
    def select_spell_2(self):  
        selected = tk.Label(self.combat, text=f"You equipped {self.hero.inventory['Spells'][1]['name']}!!", font=("Arial", 50), bg="purple")
        selected.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
        self.hero.equipped_spell = self.hero.inventory["Spells"][1]
        self.combat.update_idletasks()
        self.combat.after(1000, selected.destroy)
        self.combat.after(1000, self.buttons)
    def select_spell_3(self):
        selected = tk.Label(self.combat, text=f"You equipped {self.hero.inventory['Spells'][2]['name']}!!", font=("Arial", 50), bg="purple")
        selected.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
        self.hero.equipped_spell = self.hero.inventory["Spells"][2]
        self.combat.update_idletasks()
        self.combat.after(1000, selected.destroy)
        self.combat.after(1000, self.buttons)
    def hero_spell_attack(self):
        self.turn = False
        if self.enemy.armor > 0:
            dmg = self.hero.spell(self.hero.equipped_spell, self.enemy, self.hero.dot) 
            if self.hero.dot == 0:
                self.fdmg = tk.Label (self.combat, text=f"you did {dmg} damage to its armor!!", font=("Arial", 20), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
            else:
                self.fdmg = tk.Label (self.combat, text=f"you did {dmg} damage ({self.hero.dot} poison damage) to its armor!!", font=("Arial", 30), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
        else:
            dmg = self.hero.spell(self.hero.equipped_spell, self.enemy, self.hero.dot)
            if self.hero.dot == 0:
                self.fdmg = tk.Label (self.combat, text=f"{dmg} damage!!", font=("Arial", 20), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
            else:
                self.fdmg = tk.Label (self.combat, text=f"{dmg} damage!! ({self.hero.dot} poison damage)", font=("Arial", 30), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
        if self.hero.equipped_spell["secondary"] == "stun":
            x = random.randint(1, 2)
            if x == 1:
                self.turn = True
                stun = tk.Label(self.combat, text=f"The {self.enemy.species} was stunned and will miss their next turn!!", font=("Arial", 20), bg="purple")
                stun.place(relx=0.5, rely=0.2, anchor=tk.CENTER, height=100, width=1000)
                self.combat.update_idletasks()
                self.combat.after(2000, stun.destroy)
        if self.hero.equipped_spell["secondary"] == "poison":
            poison = tk.Label(self.combat, text=f"The {self.enemy.species} was poisoned and will take damage every turn!!", font=("Arial", 20), bg="purple")
            poison.place(relx=0.5, rely=0.7, anchor=tk.CENTER, height=100, width=1000)
            self.hero.dot = 3
            self.combat.update_idletasks()
            self.combat.after(1000, poison.destroy)
        self.hero.mana -= self.hero.equipped_spell["mana_req"]
        self.healthbare()
        self.combat.after(1000,self.determine_dead)
    def weapon_window(self):
        self.weapon_pouch.destroy()
        self.potion_pouch.destroy()
        self.spell_wheel.destroy()
        weapon1 = tk.Button(self.combat, text=self.hero.inventory["Weapons"][0]["name"], font=("Arial", 60), command=lambda: [self.select_weapon_1(), weapon1.destroy(), weapon2.destroy()])
        weapon1.place(relx=0.2, rely=0.8, anchor=tk.CENTER, width=500, height=250)
        weapon2 = tk.Button(self.combat, text=self.hero.inventory["Weapons"][1]["name"], font=("Arial", 60), command=lambda: [self.select_weapon_2(), weapon1.destroy(), weapon2.destroy()])
        weapon2.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=500, height=250)
    def select_weapon_1(self):
        selected = tk.Label(self.combat, text=f"You equipped {self.hero.inventory["Weapons"][0]['name']}!!", font=("Arial", 50), bg="purple")
        selected.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
        self.weapon = 0
        self.combat.update_idletasks()
        self.combat.after(1000, selected.destroy)
        self.combat.after(1000, self.buttons)
    def select_weapon_2(self):
        selected = tk.Label(self.combat, text=f"You equipped {self.hero.inventory["Weapons"][1]['name']}!!", font=("Arial", 50), bg="purple")
        selected.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=1000)
        self.weapon = 1
        self.combat.update_idletasks()
        self.combat.after(1000, selected.destroy)
        self.combat.after(1000, self.buttons)
    def hero_strike(self):
        self.turn = False
        dmg = self.hero.attack(self.enemy, self.active_strength, self.hero.dot) 
        if self.enemy.armor > 0:
            if self.hero.dot == 0:
                self.fdmg = tk.Label (self.combat, text=f"you did {dmg} damage to its armor!!", font=("Arial", 20), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
            else:
                self.fdmg = tk.Label (self.combat, text=f"you did {dmg} damage ({self.hero.dot} poison damage) to its armor!!", font=("Arial", 30), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
        else:
            if self.hero.dot == 0:
                self.fdmg = tk.Label (self.combat, text=f"{dmg} damage!!", font=("Arial", 20), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
            else:
                self.fdmg = tk.Label (self.combat, text=f"{dmg} damage!! ({self.hero.dot} poison damage)", font=("Arial", 30), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
        self.healthbare()
        self.combat.after(1000,self.determine_dead)
    def healthbarf(self):
        self.healthbarfgf.destroy()
        hp = self.hero.health
        health_percentagef = hp / self.max_hp
        self.healthbarfgf = tk.Label(self.combat, bg="red")
        self.healthbarfgf.place(relx=0.23, rely=0.2, anchor=tk.CENTER, width=300 * health_percentagef, height=50)
    def healthbare(self):
        self.healthbarfg.destroy()
        enemy_hp = self.enemy.hp
        health_percentage = enemy_hp / self.enemy_max_hp
        self.healthbarfg = tk.Label(self.combat, bg="red")
        self.healthbarfg.place(relx=0.8, rely=0.2, anchor=tk.CENTER, width=300 * health_percentage, height=50)
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
            self.combat.after(1000, self.spell_attack.destroy)
            self.combat.after(1000, self.combat_loop)
    def ene_turn(self):
        self.turn = True
        if self.enemy.species == "slime":
            edmg, psn = self.enemy.strike(self.hero)
            self.endmg = tk.Label (self.combat, text=f"you took {edmg} damage!! ({psn} poison damge)",wraplength= 250,  font=("Arial", 30), bg="purple")
        elif self.enemy.species == "witch":
            dmg, x = self.enemy.strike(self.hero, self)
            if x == 1:
                self.endmg = tk.Label (self.combat, text=f"you took {dmg} damage!!", font=("Arial", 20), bg="purple")
            elif x == 2:
                self.endmg = tk.Label (self.combat, text=f"you took {dmg} damage!! and were bound (will lose turn)", font=("Arial", 20), bg="purple")
            elif x == 3:
                self.endmg = tk.Label (self.combat, text=f"you took {dmg} damage!! and your strength was decreased", font=("Arial", 20), bg="purple")

        else:
            edmg = self.enemy.strike(self.hero)
            self.endmg = tk.Label (self.combat, text=f"you took {edmg} damage!!", font=("Arial", 30), bg="purple")
        self.endmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=200, width=700)
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
        self.turn = False
        dmg = self.hero.weapon_attack(self.enemy, self.hero.inventory["Weapons"][self.weapon]["dmg"], self.active_strength, self.hero.dot) 
        if self.enemy.armor > 0:
            if self.hero.dot == 0:
                self.fdmg = tk.Label (self.combat, text=f"you did {dmg} damage to its armor!!", font=("Arial", 20), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
            else:
                self.fdmg = tk.Label (self.combat, text=f"you did {dmg} damage ({self.hero.dot} poison damage) to its armor!!", font=("Arial", 30), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
        else:
            if self.hero.dot == 0:
                self.fdmg = tk.Label (self.combat, text=f"{dmg} damage!!", font=("Arial", 20), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
            else:
                self.fdmg = tk.Label (self.combat, text=f"{dmg} damage!! ({self.hero.dot} poison damage)", font=("Arial", 30), bg="purple")
                self.fdmg.place(relx=0.5, rely=0.5, anchor=tk.CENTER, height=100, width=700)
        self.healthbare()
        self.combat.after(1000,self.determine_dead)
    def fight(self):
        self.determine_enemy()
        self.healthbarf()
        self.healthbare()
        self.buttons()
        self.combat.mainloop()
    