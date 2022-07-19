from advanced_template.views.base_view import BaseView
from advanced_template.special_scripts import BasicButton
import arcade
import arcade.gui

class SettingsView(BaseView):
    def __init__(self):
        """
        This is the view that allows the user to change the settings. This will be over layered with the original view.
        """
        super().__init__(view_name="settings")

    def setup(self):
        super().setup()
        arcade.set_background_color(arcade.color.REGALIA)  # Arcade uses color not colour!)


    def on_show_view(self):
        super().on_show_view()

    def on_hide_view(self):
        super().on_hide_view()

    def on_draw(self):
        arcade.start_render()
        self.clear()
        self.ui_manager.draw()
        arcade.draw_text(
            "Settings",
            self.window.width / 2,
            self.window.height - 100,
            arcade.color.BLACK,
            font_size=80,
            anchor_x="center",
            anchor_y="center"
        )


# class SettingsView(BaseView):
#     def __init__(self):
#         """
#         This is the view that allows the user to change the settings. This will be over layered with the original view.
#         """
#         super().__init__(view_name="settings")
#
#     def on_show_view(self, parent_view, draw_previous):
#         """
#         :param parent_view: The view that came before the settings. This is necessary for overlapping the views.
#         :param draw_previous: If the previous view should be drawn. If so, True.
#         """
#         super().on_show_view(force_setup=True)
#         self.parent_view = parent_view
#         self.draw_previous = draw_previous
#
#     def setup(self):
#         super().setup()
#         arcade.set_background_color(arcade.color.BLUEBERRY)  # Arcade uses color not colour!)
#         self.setup_buttons()
#
#     def setup_buttons(self):
#         self.ui_manager = arcade.gui.UIManager()
#
#     def on_draw(self):
#         arcade.start_render()
#
#         self.clear()
#
#         self.ui_manager.draw()
#
#         if self.draw_previous is True:
#             self.game_view.ui_manager.draw()
#
#         arcade.draw_text(
#             "Settings",
#             self.window.width / 2,
#             self.window.height - 100,
#             arcade.color.BLACK,
#             font_size=80,
#             anchor_x="center",
#             anchor_y="center",
#         )
#
#     def on_key_press(self, key: int, modifiers: int):
#         if key == arcade.key.ESCAPE:
#             self.changing_view_with_key(key=key, modifiers=modifiers, current_view=self,
#                                         new_view=self.window.views["main_menu"])
#             self.window.show_view(self.window.views["main_menu"])
#
#     @property
#     def parent_view(self):
#         """
#         This is the view that precided the settings view.
#         """
#         return self._parent_view
#
#     @parent_view.setter
#     def game_view(self, value: arcade.View):
#         self._parent_view = value
#
#     @property
#     def draw_previous(self):
#         """
#         If the previous view should be drawn. If so, True.
#         This will be used to avoid layering views when i don't want to do that (e.g. the main menu)
#         """
#         return self._draw_previous
#
#     @draw_previous.setter
#     def draw_previous(self, value: bool):
#         self._draw_previous = value
