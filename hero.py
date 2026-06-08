import random
import monster

class hero():
    def __init__(self,money, inventory, hunger,health,strength,equipped_spell,level,charisma,xp_req,xp,armor,mana, dot, max_hp):
        self.money = money
        self.inventory = inventory
        self.hunger = hunger
        self.health = health
        self.strength = strength
        self.equipped_spell = equipped_spell
        self.level = level
        self.charisma = charisma
        self.xp_req = xp_req
        self.xp = xp
        self.armor = armor
        self.mana = mana
        self.dot = dot
        self.max_hp = max_hp
    def generate(self):
        self.health += self.level * 1.5 
        self.strength += self.level * 2
        self.mana += self.level * 2
        self.max_hp = self.health


    def attack(self, monster, strength,dot):
        dmg =(1*(1+(strength/100))) + dot
        dmg = round(dmg)
        if monster.armor < 0 or monster.armor == 0:
            monster.hp -= dmg
        else:
            monster.armor -= dmg
        if monster.hp < 0:
            monster.hp = 0
        if monster.hp == 0:
            monster.dead = True
        return dmg

    def weapon_attack(self, monster, weapon, strength, dot):
        dmg = (weapon *(strength/10)) + dot
        dmg = round(dmg)
        if monster.armor < 0 or monster.armor == 0:
            monster.hp -= dmg
        else:
            monster.armor -= dmg
        if monster.hp < 0:
            monster.hp = 0
        if monster.hp == 0:
            monster.dead = True
        return dmg


    
    def spell(self,equipped_spell, monster, dot):
        dmg = equipped_spell["damage"] + dot
        dmg = round(dmg)
        if monster.armor < 0 or monster.armor == 0:
            monster.hp -= dmg
        else:
            monster.armor -= dmg
        if monster.hp < 0:
            monster.hp = 0
        if monster.hp == 0:
            monster.dead = True
        return dmg

    def level(self,xp,xp_req,level):
        if self.xp >= self.xp_req:
            self.level+=1
            self.xp_req +=10
            self.xp = 0

        



