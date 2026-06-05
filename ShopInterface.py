import arcade
import arcade.gui
from hero import hero

class ShopInterface(arcade.View):
    def __init__(self, player_hero: hero, game_view):
        super().__init__()
        self.background_color = arcade.color.DARK_SLATE_GRAY
        self.game_view = game_view
        self.ui = arcade.gui.UIManager()
        self.ui.enable()
        self.player_hero = player_hero

        v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=25)

        title_label = arcade.gui.UILabel(text="SHOP", text_color=arcade.color.GOLD, font_size=60)
        v_box.add(title_label)

        gold_label = arcade.gui.UILabel(text=f"gold: {self.player_hero.money}", text_color=arcade.color.YELLOW, font_size=32)
        v_box.add(gold_label)
        self.gold_label = gold_label

        buy_sword_button = arcade.gui.UIFlatButton(text="  buy sword - 100 gold", width=400, height=80)
        buy_sword_button.on_click = self.on_buy_sword
        v_box.add(buy_sword_button)
            
        buy_shield_button = arcade.gui.UIFlatButton(text="  buy shield - 150 gold", width=400, height=80)
        buy_shield_button.on_click = self.on_buy_shield
        v_box.add(buy_shield_button)

        buy_potion_button = arcade.gui.UIFlatButton(text=" buy health potion - 50 gold", width=400, height=80)
        buy_potion_button.on_click = self.on_buy_potion
        v_box.add(buy_potion_button)

        close_button = arcade.gui.UIFlatButton(text="Close (ESC)", width=400, height=80)
        close_button.on_click = self.on_close
        v_box.add(close_button)

        anchor_box = arcade.gui.UIAnchorLayout()
        anchor_box.add(child=v_box, anchor_x="center_x", anchor_y="center_y")
        self.ui.add(anchor_box)

    def on_draw(self):
        self.clear()
        self.ui.draw()

    def on_buy_sword(self, event):
        if self.player_hero.money >= 100:
            self.player_hero.money -= 100
            self.player_hero.inventory.append("sword")
            self.player_hero.strength += 5
            print("bought sword")
            self.gold_label.text = f"gold: {self.player_hero.money}"
        else:
            print("not enough gold")

    def on_buy_shield(self, event):
        if self.player_hero.money >= 150:
            self.player_hero.money -= 150
            self.player_hero.inventory.append("shield")
            self.player_hero.armor += 10
            print("bought shield")
            self.gold_label.text = f"gold: {self.player_hero.money}"
        else:
            print("not enough gold")

    def on_buy_potion(self, event):
        if self.player_hero.money >= 50:
            self.player_hero.money -= 50
            self.player_hero.inventory.append("health_potion")
            print("bought health potion")
            self.gold_label.text = f"gold: {self.player_hero.money}"
        else:
            print("not enough gold")

    def on_close(self, event):
        self.window.show_view(self.game_view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)