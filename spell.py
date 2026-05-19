import arcade
import arcade.gui
from hero import hero

class SpellShopInterface(arcade.View):
    def __init__(self, player_hero: hero, game_view):
        super().__init__()
        self.background_color = arcade.color.DARK_SLATE_GRAY
        self.player_hero = player_hero
        self.game_view = game_view
        self.ui = arcade.gui.UIManager()
        self.ui.enable()

        v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=25)

        title_label = arcade.gui.UILabel(text="SPELLS", text_color=arcade.color.GOLD, font_size=60)
        v_box.add(title_label)
        
        level_label = arcade.gui.UILabel(text=f"level: {self.player_hero.level}", text_color=arcade.color.YELLOW, font_size=32)
        v_box.add(level_label)
        
        current_spell_label = arcade.gui.UILabel(text=f"equipped: {self.player_hero.equipped_spell or 'none'}", text_color=arcade.color.LIGHT_CYAN, font_size=24)
        v_box.add(current_spell_label)
        self.current_spell_label = current_spell_label

        self.spells = [
            {"name": "fireball", "damage": 25, "level_req": 1},
            {"name": "ice_storm", "damage": 35, "level_req": 3},
            {"name": "meteor", "damage": 50, "level_req": 5},
            {"name": "lightning", "damage": 40, "level_req": 4},
        ]

        can_equip = self.player_hero.level >= self.spells[0]["level_req"]
        spell_button1 = arcade.gui.UIFlatButton(text=f"{self.spells[0]['name']} - dmg: {self.spells[0]['damage']} (req: Lvl {self.spells[0]['level_req']})", width=400, height=70)
        spell_button1.on_click = self.button1_click
        v_box.add(spell_button1)

        can_equip = self.player_hero.level >= self.spells[1]["level_req"]
        spell_button2 = arcade.gui.UIFlatButton(text=f"{self.spells[1]['name']} - dmg: {self.spells[1]['damage']} (req: Lvl {self.spells[1]['level_req']})", width=400, height=70)
        spell_button2.on_click = self.button2_click
        v_box.add(spell_button2)

        can_equip = self.player_hero.level >= self.spells[2]["level_req"]
        spell_button3 = arcade.gui.UIFlatButton(text=f"{self.spells[2]['name']} - dmg: {self.spells[2]['damage']} (req: Lvl {self.spells[2]['level_req']})", width=400, height=70)
        spell_button3.on_click = self.button3_click
        v_box.add(spell_button3)

        can_equip = self.player_hero.level >= self.spells[3]["level_req"]
        spell_button4 = arcade.gui.UIFlatButton(text=f"{self.spells[3]['name']} - dmg: {self.spells[3]['damage']} (req: Lvl {self.spells[3]['level_req']})", width=400, height=70)
        spell_button4.on_click = self.button4_click
        v_box.add(spell_button4)

        close_button = arcade.gui.UIFlatButton(text="close (ESC)", width=400, height=80)
        close_button.on_click = self.on_close
        v_box.add(close_button)

        anchor_box = arcade.gui.UIAnchorLayout()
        anchor_box.add(child=v_box, anchor_x="center_x", anchor_y="center_y")
        self.ui.add(anchor_box)

    def on_draw(self):
        self.clear()
        self.ui.draw()
    
    def button1_click(self, event):
        self.on_equip_spell(self.spells[0]["name"], self.spells[0]["level_req"])

    def button2_click(self, event):
        self.on_equip_spell(self.spells[1]["name"], self.spells[1]["level_req"])

    def button3_click(self, event):
        self.on_equip_spell(self.spells[2]["name"], self.spells[2]["level_req"])

    def button4_click(self, event):
        self.on_equip_spell(self.spells[3]["name"], self.spells[3]["level_req"])

    def on_equip_spell(self, spell_name, level_req):
        if self.player_hero.level >= level_req:
            self.player_hero.equipped_spell = spell_name
            self.current_spell_label.text = f"equipped: {spell_name.upper()}"
            print(f"equipped {spell_name}")
        else:
            print(f"you need level {level_req} to equip {spell_name}")

    def on_close(self, event):
        self.window.show_view(self.game_view)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)