import random
import arcade

SPRITE_SCALING = 5
WALL_SCALING = 5
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1280
WINDOW_TITLE = "The Unbinding of Isaac"
VIEWPORT_MARGIN = 600

HORIZONTAL_BOUNDARY = 300
VERTICAL_BOUNDARY = 300

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
        self.camera_sprites = arcade.Camera2D()
        self.camera_gui = arcade.Camera2D()
    def setup(self):

        layer_options = {
            "Platforms": {
                "use_spatial_hash": True
            }
        }

        # Load our TileMap
        self.tile_map = arcade.load_tilemap(
            "tilemap",
            scaling=TILE_SCALING,
            layer_options=layer_options,
        )

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.player_texture = arcade.load_texture(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        )

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls=self.scene["object layer"], gravity_constant=GRAVITY
        )

        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("sprite.png", SPRITE_SCALING)
        self.player_list.append(self.player_sprite)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        self.background_color = arcade.color.BISTRE
    def on_draw(self):
        self.clear()
        self.camera_sprites.use()
        self.player_list.draw()
        self.wall_list.draw()
        self.camera_gui.use()
        arcade.draw_lrbt_rectangle_filled(0, self.width, 0, 40, arcade.color.BISTRE)
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
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
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game = Interface()
    game.setup()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()