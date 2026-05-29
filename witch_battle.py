import monster
import random 
import tkinter as tk
import hero
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
        hero.health -= 10
        self.mana -= 5
    def bind(self, player):
        hero.health -= 2
        "skip next player turn"
        self.mana -= 12
    def weaken(self, player):
        hero.health -= 2
        hero.attack -= 4
        self.mana -= 8
        def generate(self):
            self.attack = self.level * 1.5
            self.hp = self.level * 2
            self.mana = self.level * 1.7