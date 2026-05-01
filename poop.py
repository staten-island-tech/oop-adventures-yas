import arcade

# --- Constants (these are fixed values we can reuse) ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Simple Arcade Example"

PLAYER_SIZE = 50
PLAYER_SPEED = 5


# --- Main Game Class ---
class MyGame(arcade.Window):
    """Main application class"""

    def __init__(self):
        # Call the parent class (arcade.Window) constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE)

        # Player position (start in the middle of screen)
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        """Called every time the screen needs to be drawn"""
        # Start drawing (clears the screen)
        arcade.start_render()

        # Draw a rectangle (our "player")
        arcade.draw_rectangle_filled(
            self.player_x,
            self.player_y,
            PLAYER_SIZE,
            PLAYER_SIZE,
            arcade.color.WHITE
        )

    def on_key_press(self, key, modifiers):
        """Called when a key is pressed"""
        if key == arcade.key.UP:
            self.player_y += PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player_y -= PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player_x -= PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_x += PLAYER_SPEED

    def on_update(self, delta_time):
        """Game logic updates go here (runs ~60 times per second)"""
        # This example doesn't need continuous updates yet
        pass


# --- Main function ---
def main():
    """Start the game"""
    game = MyGame()
    arcade.run()


# Run the program
if __name__ == "__main__":
    main()