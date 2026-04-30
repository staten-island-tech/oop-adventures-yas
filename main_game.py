import hero
import random
import monster
import math

player = hero.hero(10,100,100,1,1,1,4,100,50,0,0)
goblin = monster.goblin("hp","attack",1)
witch = monster.witch("hp","attack",1, 10)
skeleton = monster.skeleton("hp","attack",1, 10)
slime = monster.slime("hp","attack",1)




""" goblin.generate()
player.attack(goblin, 1)
print(goblin.hp)
player.attack(goblin, 1)
print(goblin.hp) """
