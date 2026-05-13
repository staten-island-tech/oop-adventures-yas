import arcade
import arcade.gui
from hero import hero

class ShopInterface(arcade.View):
    def __init__(self, player_hero: hero):
        super().__init__()
        self.background_color = arcade.color.BROWN
        self.player_hero = player_hero
        self.ui = arcade.gui.UIManager()
        self.ui.enable()

        v_box = arcade.gui.UIBoxLayout()
        buy_sword_button = arcade.gui.UIFlatButton(text="buy Sword - 100 Gold", width=200)
        buy_sword_button.on_click = self.on_buy_sword
        v_box.add(buy_sword_button)
            
        buy_shield_button = arcade.gui.UIFlatButton(text="buy Shield - 150 Gold", width=200)
        buy_shield_button.on_click = self.on_buy_shield
        v_box.add(buy_shield_button)

        buy_potion_button = arcade.gui.UIFlatButton(text="buy Health Potion - 50 Gold", width=200)
        buy_potion_button.on_click = self.on_buy_potion
        v_box.add(buy_potion_button)

        close_button = arcade.gui.UIFlatButton(text="close", width=200)
        close_button.on_click = self.on_close
        v_box.add(close_button)

        self.ui.add(v_box)

    def on_draw(self):
        self.clear()
        arcade.draw_text("welcome to the shop, press ESC to close (or close button)", 10, 550, arcade.color.WHITE, 14)
        arcade.draw_text(f"Gold: {self.player_hero.money}", 10, 520, arcade.color.YELLOW, 14)
        self.ui.draw()

    def on_buy_sword(self, event):
        if self.player_hero.money >= 100:
            self.player_hero.money -= 100
            self.player_hero.inventory.append("sword")
            self.player_hero.strength += 5
            print("bought sword")
        else:
            print("not enough gold")

    def on_buy_shield(self, event):
        if self.player_hero.money >= 150:
            self.player_hero.money -= 150
            self.player_hero.inventory.append("shield")
            self.player_hero.armor += 10
            print("bought shield!")
        else:
            print("not enough gold")

    def on_buy_potion(self, event):
        if self.player_hero.money >= 50:
            self.player_hero.money -= 50
            self.player_hero.inventory.append("health_potion")
            print("bought health potion")
        else:
            print("not enough gold")

    def on_close(self, event):
        arcade.show_view(game)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.show_view(game)