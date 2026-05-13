import random
import monster
import math
class hero():
    def __init__(self,money,hunger,health,strength,equipped_spell,level,charisma,xp_req,xp,stat_points,armor):
        self.money = money
        self.inventory = []
        self.hunger = hunger
        self.health = health
        self.strength = strength
        self.equipped_spell = equipped_spell
        self.level = level
        self.charisma = charisma
        self.xp_req = xp_req
        self.xp = xp
        self.stat_points = stat_points
        self.armor = armor

    def attack(self, monster, strength,):
        monster.hp -=1*(1+(strength/100))
        monster.hp = math.ceil(monster.hp)
        if monster.hp < 0:
            monster.hp = 0
        if monster.hp == 0:
            print(f"You defeated {monster.species}!")

    def heal(self,health,inventory):
        for i in self.inventory:
            if "health_potion" in self.inventory[i]:
                self.health += "health_potion"[heal]
    
    def spell(self,equipped_spell):
        monster.hp -= equipped_spell['damage']

    def level(self,xp,xp_req,level,stat_points):
        if self.xp >= self.xp_req:
            self.level+=1
            self.xp_req +=10
            self.xp = 0
            self.stat_points +=1
        

     
    

        