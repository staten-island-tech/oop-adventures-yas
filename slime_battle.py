from monster import monster
import random 
import tkinter as tk
import math


class slime(monster):
    def __init__(self, hp, attack, level, dead, dot):
        super().__init__("slime", hp, attack, level, dead)
        self.dot = dot
    def strike(self, hero):
        hurt = (self.attack * 1.5)
        hero.health -= hurt
        round(hero.health)
        self.dot += 2
        if self.dot > 10:
            self.dot = 10
        hero.health -= self.dot
        edmg = round(hurt + self.dot)
        return edmg, self.dot
        



