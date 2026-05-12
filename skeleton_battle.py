import random 
import monster 
import tkinter as tk

class skeleton(monster):
    def __init__(self, hp, attack, level, armor, weapon_dmg):
        super().__init__("skeleton", hp, attack, level)
        self.armor = armor
        self.weapon_dmg = weapon_dmg
    def generate(self):
        x= random.randint(1,5)
        self.weapon_dmg = (self.level/10)+x
        return super().generate()
    def strike(self):
        hurt = ((self.attack * 1.5)+self.weapon_dmg)-"player armor"
        "player health - hurt"       
    def take_damage(self, damage):
        self.hp -= damage - self.armor
