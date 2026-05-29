from monster import monster
import random 
import tkinter as tk
import hero


class goblin(monster):
    def __init__(self, hp, attack, level, dead):
        self.hp = hp
        self.attack = attack
        self.level = level
        self.dead = dead
    def slash(self,hp,attack,level):
        damage = (1+attack*(level/100))
        hero.health -= damage
        print(f"The goblin slashes for {damage} damage!")
    def punch(self):
        damage = (self.attack)
        hero.health -= damage
        print(f"The goblin punches for {damage} damage!")
        