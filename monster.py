import random

class monster():
    def __init__(self, species, hp, attack, level):
        self.species = species
        self.hp = hp
        self.attack = attack
        self.level = level
    def take_damage(self, damage):
        self.hp -= damage
    def strike(self):
        hurt = (self.attack * 1.5)-"player armor"
        "player health - hurt"
    def generate(self):
        self.attack = self.level * 1.5
        self.hp = self.level * 2


    
class skeleton(monster):
    def __init__(self, hp, attack, level, armor, weapon_dmg):
        super().__init__("skeleton", hp, attack, level)
        self.armor = armor
        self.weapon_dmg = weapon_dmg
    def generate(self):
        x= random.randint(1,5)
        self.weapon_dmg = (self.level/10)+x
        return super().generate()
    def strike(self):
        hurt = ((self.attack * 1.5)+self.weapon_dmg)-"player armor"
        "player health - hurt"       
    def take_damage(self, damage):
        self.hp -= damage - self.armor

class witch(monster):
    def __init__(self, hp, attack, level,mana):
        super().__init__("witch", hp, attack, level)
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

class goblin(monster):
    def __init__(self, hp, attack, level):
        super().__init__("goblin", hp, attack, level)

class slime(monster):
    def __init__(self, hp, attack, level):
        super().__init__("slime", hp, attack, level)
    def strike(self):
        hurt = (self.attack * 1.5)
        "player health - hurt"