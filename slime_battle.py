import monster
import random 
import tkinter as tk

class slime(monster):
    def __init__(self, hp, attack, level):
        super().__init__("slime", hp, attack, level)
    def strike(self):
        hurt = (self.attack * 1.5)
        "player health - hurt"