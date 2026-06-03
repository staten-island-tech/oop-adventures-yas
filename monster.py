import random

class monster():
    def __init__(self, species, hp, attack, level, dead, armor):
        self.species = species
        self.hp = hp
        self.attack = attack
        self.level = level
        self.dead = False
        self.stunned = False
        self.armor = armor
    def strike(self):
        hurt = (self.attack * 1.5)-"player armor"
        "player health - hurt"
    def generate(self):
        self.attack = self.level * 1.5
        self.hp = self.level * 2





