from monster import monster
import random 
import tkinter as tk


class goblin(monster):
    def __init__(self, hp, attack, level, dead):
        super().__init__("goblin", hp, attack, level, dead)

