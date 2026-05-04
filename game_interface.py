import random
import arcade

SPRITE_SCALING = 0.5
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
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("sprite.png")
        self.wall_sprite = arcade.Sprite("wall.png")
        self.wall_list.append(self.wall_sprite)
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

def main():
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
     # Create and setup the GameView
    game = Interface()
    game.setup()
    # Show GameView on screen
    window.show_view(game)

        # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()