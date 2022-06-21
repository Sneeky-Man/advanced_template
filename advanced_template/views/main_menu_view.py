from advanced_template.views import BaseView
import arcade


class MainMenuView(BaseView):
    def __init__(self):
        super().__init__(view_name="main_menu")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLUEBERRY)  # Arcade uses color not colour!)

    def on_draw(self):
        arcade.start_render()