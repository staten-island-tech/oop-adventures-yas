import arcade
import shopkeep

class ShopInterface(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK

    def on_draw(self):
        self.clear()
        arcade.draw_text("Welcome to the Shop, press ESC to close", 10, 10, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()


def main():
    window = arcade.Window(800, 600, "Shop")
    shop_view = ShopInterface()
    window.show_view(shop_view)
    arcade.run()

if __name__ == "__main__":
    main()