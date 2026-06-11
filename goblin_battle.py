from monster import monster
import random 
import tkinter as tk
import hero


class goblin(monster):
    def __init__(self, hp, attack, level, dead):
        super().__init__("goblin", hp, attack, level, dead, 0)
    def strike(self, hero):
        hurt = (self.attack * 1.25)
        hurt = round(hurt)
        hero.health -= hurt
        return hurt
