from monster import monster
import random 
import tkinter as tk

class slime(monster):
    def __init__(self, hp, attack, level, dead):
        super().__init__("slime", hp, attack, level, dead)
    def strike(self):
        hurt = (self.attack * 1.5)
