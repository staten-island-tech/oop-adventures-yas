import monster
import random 
import tkinter as tk

class witch(monster):
    def __init__(self, hp, attack, level, dead, mana):
        super().__init__("witch", hp, attack, level, dead)
        self.spells = ["fireball","bind","weaken"]
        self.mana = mana
    def attack(self):
        attack = random.choice(self.spells)
        if attack == "fireball":
            self.fireball()
        elif attack == "bind":
            self.bind()
        elif attack == "weaken":
            self.weaken()
    def fireball(self, player):
        "player.hp-=10"
        self.mana -= 5
    def bind(self, player):
        "player.hp -=2"
        "skip next player turn"
        self.mana -= 12
    def weaken(self, player):
        "player.hp -=2"
        "weaken next player attack"
        self.mana -= 8
        def generate(self):
            self.attack = self.level * 1.5
            self.hp = self.level * 2
            self.mana = self.level *1.7