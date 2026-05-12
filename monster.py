import random

class monster():
    def __init__(self, species, hp, attack, level):
        self.species = species
        self.hp = hp
        self.attack = attack
        self.level = level
    def strike(self):
        hurt = (self.attack * 1.5)-"player armor"
        "player health - hurt"
    def generate(self):
        self.attack = self.level * 1.5
        self.hp = self.level * 2





