from monster import monster
import random 
import tkinter as tk
import hero


class goblin(monster):
    def __init__(self, hp, attack, level, dead):
        super().__init__("goblin", hp, attack, level, dead, 0)
    def strike(self, hero):
        hurt = (self.attack * 1.5)
        hero.health -= hurt
        round(hero.health)
        return hurt
