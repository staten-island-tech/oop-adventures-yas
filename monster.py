import random
class monster():
    def __init__(self, species, hp, attack, level):
        self.species = species
        self.hp = hp
        self.attack = attack
        self.level = level
    def take_damage(self, damage):
        self.hp -= damage
    
class skeleton(monster):
    def __init__(self, hp, attack, level, armor):
        super().__init__("skeleton", hp, attack, level)
        self.armor = armor

class witch(monster):
    def __init__(self, hp, attack, level, spells=None):
        super().__init__("witch", hp, attack, level)
        self.spells = spells or ["fireball", "bind", "weaken"]
    def attack(self, player):
        spell = random.choice(self.spells)
        getattr(self, spell)(player)
    def fireball(self, player):
        player.hp-=10
    def bind(self, player):
        player.hp -=2
        "skip next player turn"
    def weaken(self, player):
        player.hp -=2
        "weaken next player attack"

class goblin(monster):
    def __init__(self, hp, attack, level):
        super().__init__("goblin", hp, attack, level)