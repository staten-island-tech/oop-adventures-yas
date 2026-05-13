import arcade
import shopkeep
from hero import hero
import arcade.gui

class ShopInterface(arcade.View):
    def __init__(self, player_hero: hero):
        super().__init__()
        self.background_color = arcade.color.BROWN
        self.player_hero = player_hero
        self.ui = arcade.gui.UIManager()
        self.ui.enable()

        v_box = arcade.gui.UIBoxLayout()
    
        buy_sword_btn = arcade.gui.UIFlatButton(text="Buy Sword - 100 Gold", width=200)
        buy_sword_btn.on_click = self.on_buy_sword
        v_box.add(buy_sword_btn)
        
        buy_shield_btn = arcade.gui.UIFlatButton(text="Buy Shield - 150 Gold", width=200)
        buy_shield_btn.on_click = self.on_buy_shield
        v_box.add(buy_shield_btn)
        
        buy_potion_btn = arcade.gui.UIFlatButton(text="Buy Health Potion - 50 Gold", width=200)
        buy_potion_btn.on_click = self.on_buy_potion
        v_box.add(buy_potion_btn)
        
        close_btn = arcade.gui.UIFlatButton(text="Close (ESC)", width=200)
        close_btn.on_click = self.on_close
        v_box.add(close_btn)
        
        self.ui.add(v_box, anchor_x="center", anchor_y="center")

    def on_draw(self):
        self.clear()
        arcade.draw_text("welcome to the shop, press ESC to close", 10, 550, arcade.color.WHITE, 14)
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
        from game_interface import Interface
        game = Interface()
        game.setup()
        self.window.show_view(game)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            from game_interface import Interface
            game = Interface()
            game.setup()
            self.window.show_view(game)