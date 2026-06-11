from monster import monster
import random 


class witch(monster):
    def __init__(self, hp, attack, level, dead):
        super().__init__("witch", hp, attack, level, dead, 0)
        self.spells = ["fireball","bind","weaken"]
    def strike(self, hero, a):
        attack = random.choice(self.spells)
        if attack == "fireball":
            return self.fireball(hero)
        elif attack == "bind":
            return self.bind(hero, a)
        elif attack == "weaken":
            return self.weaken(hero, a)
    def fireball(self, hero):
        dmg = self.attack * 2
        dmg = round(dmg)
        hero.health -= dmg
        x=1
        return dmg, x 
    def bind(self, hero, a):
        dmg = self.attack * 1.1
        dmg = round(dmg)
        hero.health -= dmg
        a.turn = False
        x=2
        return dmg, x
    def weaken(self, hero, a):
        dmg = self.attack * 1.1
        dmg = round(dmg)
        hero.health -= dmg
        a.active_strength -= 4
        x=3
        return dmg, x