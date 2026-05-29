import random
import arcade
from ShopInterface import ShopInterface
from hero import hero
from spell import SpellShopInterface
from arcade.future.light import Light, LightLayer
import monster

AMBIENT_COLOR = (20, 20, 20)
SPRITE_SCALING = 3.5
WALL_SCALING = 4
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1280
WINDOW_TITLE = "The Unbinding of Isaac"
VIEWPORT_MARGIN = 600
GRAVITY = 0


CAMERA_SPEED = 0.1
PLAYER_MOVEMENT_SPEED = 3

class Interface(arcade.View):
    def __init__(self):
        super().__init__()
        self.player_sprite = None
        self.wall_sprite = None
        self.physics_engine = None
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.tile_map = None
        self.camera_sprites = arcade.Camera2D()
        self.camera_gui = arcade.Camera2D()
        self.player_hero = hero(money=500, inventory=[], hunger=100, health=100, strength=10, equipped_spell=None, level=1, charisma=5, xp_req=100, xp=0, stat_points=0, armor=5, mana=100)
        self.monster_list = monster
        self.player_light = None
    def setup(self):

        layer_options = {
            "Platforms": {
                "use_spatial_hash": True
            }
        }


        self.tile_map = arcade.load_tilemap(
            "main_map.json",
            scaling=WALL_SCALING,
            layer_options=layer_options,
        )

        self.scene = arcade.Scene.from_tilemap(self.tile_map)



        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("game_sprite.png", SPRITE_SCALING)
        self.player_list.append(self.player_sprite)
        self.light_layer = LightLayer(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, walls=self.scene["Object_Layer"]
        )
        radius = 200
        mode = 'soft'
        color = arcade.csscolor.WHITE
        self.player_light = Light(0, 0, radius, color, mode)

        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 3000
        
        self.background_color = arcade.color.BISTRE

        pass

    def on_draw(self):
        self.clear()
        self.camera_sprites.use()
        with self.light_layer:
            self.scene.draw()
            self.player_list.draw()
        self.light_layer.draw(ambient_color=AMBIENT_COLOR)
        self.camera_gui.use()
        arcade.draw_text("press SPACE to turn lantern on/off.", 10, 10, arcade.color.WHITE, 20)
        arcade.draw_text("press O to open the spell inventory", 10, 40, arcade.color.WHITE, 20)
        arcade.draw_text("press S to open shop", 10, 70, arcade.color.WHITE, 20)
        arcade.draw_text("F11 to toggle fullscreen", 10, 100, arcade.color.WHITE, 20)
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.S:
            shop = ShopInterface(self.player_hero, self)
            self.window.show_view(shop)
        elif key == arcade.key.F11:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif key == arcade.key.O:
            spell_shop = SpellShopInterface(self.player_hero, self)
            self.window.show_view(spell_shop)
        elif key == arcade.key.SPACE:
            if self.player_light in self.light_layer:
                self.light_layer.remove(self.player_light)
            else:
                self.light_layer.add(self.player_light)
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
    def on_update(self, delta_time):
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        self.player_light.position = self.player_sprite.position
        self.physics_engine.update()
        self.scroll_to_player()
    def scroll_to_player(self):

        target_x = self.player_sprite.center_x
        target_y = self.player_sprite.center_y
        
        current_x = self.camera_sprites.position[0]
        current_y = self.camera_sprites.position[1]
        
        new_x = arcade.math.lerp(current_x, target_x, CAMERA_SPEED)
        new_y = arcade.math.lerp(current_y, target_y, CAMERA_SPEED)
        
        self.camera_sprites.position = (new_x, new_y)

    def on_resize(self, width: int, height: int):
        super().on_resize(width, height)
        self.camera_sprites.match_window()
        self.camera_gui.match_window(position=True)
def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, fullscreen=True)

    window.ctx.enable(window.ctx.BLEND)
    
    game = Interface()
    game.setup()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()


