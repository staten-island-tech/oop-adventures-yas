import random 
from monster import monster
import tkinter as tk
import hero
class skeleton(monster):
    def __init__(self, hp, attack, level, dead, armor, weapon_dmg):
        super().__init__("skeleton", hp, attack, level, dead, 20)
        self.armor = armor
        self.weapon_dmg = weapon_dmg
    def strike(self, hero):
        hurt = ((self.attack * 1.5)+self.weapon_dmg)
        hurt = round(hurt)
        hero.health -= hurt
        return hurt


