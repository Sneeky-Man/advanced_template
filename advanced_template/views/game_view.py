from advanced_template.views.base_view import BaseView
from advanced_template.views.settings_view import SettingsView
import arcade
import arcade.gui


class GameView(BaseView):
    def __init__(self):
        """
        This is the view for the main game.
        """
        super().__init__(view_name="game")

    def setup(self):
        super().setup()
        arcade.set_background_color(arcade.color.AERO_BLUE)

    def on_show_view(self):
        super().on_show_view()

    def on_hide_view(self):
        super().on_hide_view()

    def on_draw(self):
        arcade.start_render()
        self.clear()
        self.ui_manager.draw()

        arcade.draw_text("Game View!",
                         self.window.width / 2,
                         self.window.height - 400,
                         arcade.color.BLACK,
                         font_size=80,
                         anchor_x="center",
                         anchor_y="center"
                         )

#     def on_key_press(self, key: int, modifiers: int):
#         if key == arcade.key.ESCAPE:
#             print(self.window.views)
#             print(self.window.views[SettingsView.view_name].view_name)
#         # if key == arcade.key.ESCAPE:
#         #     if SettingsView.view_name not in self.window.views:
#         #         self.window.views[SettingsView.view_name] = SettingsView(game_view=self, draw_previous=False)
#         #     self.changing_view_with_key(key=key, modifiers=modifiers, current_view_name=self.view_name,
#         #                                 new_view_name=self.window.views[SettingsView.view_name].view_name)
#         #     print(self.window.views[SettingsView.view_name].view_name)
#         #     self.window.show_view(self.window.views[SettingsView.view_name])


