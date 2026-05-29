import random 
import monster 
import tkinter as tk
import hero
class skeleton(monster):
    def __init__(self, hp, attack, level, dead, armor, weapon_dmg):
        super().__init__("skeleton", hp, attack, level, dead)
        self.armor = armor
        self.weapon_dmg = weapon_dmg
    def generate(self):
        x= random.randint(1,5)
        self.weapon_dmg = (self.level/10)+x
        return super().generate()
    def strike(self):
        hurt = ((self.attack * 1.5)+self.weapon_dmg)-hero.armor
        hero.health -= hurt   

