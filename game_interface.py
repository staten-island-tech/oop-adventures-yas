import random
import arcade
from ShopInterface import ShopInterface
from hero import hero
from ShopInterface import ShopInterface
from spell import SpellShopInterface

SPRITE_SCALING = 4
WALL_SCALING = 4
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1280
WINDOW_TITLE = "The Unbinding of Isaac"
VIEWPORT_MARGIN = 600
GRAVITY = 0

HORIZONTAL_BOUNDARY = 200
VERTICAL_BOUNDARY = 100

CAMERA_BOUNDARY = arcade.LRBT(
    -HORIZONTAL_BOUNDARY,
      HORIZONTAL_BOUNDARY,
      -VERTICAL_BOUNDARY,
      VERTICAL_BOUNDARY,
)

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
        self.player_hero = hero(money=500, hunger=100, health=100, strength=10, equipped_spell=None, level=1, charisma=5, xp_req=100, xp=0, stat_points=0, armor=5)
    
    def setup(self):

        layer_options = {
            "Platforms": {
                "use_spatial_hash": True
            }
        }


        self.tile_map = arcade.load_tilemap(
            "test_map.json",
            scaling=SPRITE_SCALING,
            layer_options=layer_options,
        )

        self.scene = arcade.Scene.from_tilemap(self.tile_map)



        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("game_sprite.png", SPRITE_SCALING)
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, walls=self.scene["Object_Layer"]
        )
        

        self.player_sprite.center_x = 800
        self.player_sprite.center_y = 800
        
        self.background_color = arcade.color.BISTRE

        pass

    def on_draw(self):
        self.clear()
        self.camera_sprites.use()
        self.scene.draw()
        self.player_list.draw()
        self.camera_gui.use()
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
        self.physics_engine.update()
        self.scroll_to_player()
    def scroll_to_player(self):
        new_position = arcade.camera.grips.constrain_boundary_xy(
            self.camera_sprites.view_data, CAMERA_BOUNDARY, self.player_sprite.position
        )
        self.camera_sprites.position = arcade.math.lerp_2d(
            self.camera_sprites.position, (new_position[0], new_position[1]), CAMERA_SPEED
        )
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