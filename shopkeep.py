import hero

def shopkeep():
    def __init__(self,name,inventory):
        self.name = name
        self.inventory = inventory
    def sell(self,hero,item,price):
        if item in self.inventory:
            if hero.money >= self.inventory[item][price]:
                hero.money -= self.inventory[item][price]
                hero.inventory.append(item)
                print(f"hero bought a {item} for {self.inventory[item][price]} gold.")
            else:
                print(f"hero does not have enough gold to buy {item}")
        else:
            print(f"{item} is not available in the shop.")
    def buy(self,hero,item,price):
        if item in hero.inventory:
            hero.money += self.inventory[item][price]
            hero.inventory.remove(item)
            print(f"hero sold a {item} for {self.inventory[item]} $")
        else:
            print(f"hero does not have {item}")
    