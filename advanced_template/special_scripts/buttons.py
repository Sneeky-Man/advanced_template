"""
This will be a collection of buttons. These will largely be used on the main menu and settings.
"""

import arcade.gui
import logging
from advanced_template.path import ABSOLUTE_PATH


class BasicButton(arcade.gui.UITextureButton):
    def __init__(self, name, width=200, text=""):

        self.name = name
        self.normal_texture = "assets/images/buttons/button.png"
        self.hover_texture = "assets/images/buttons/button_hover.png"
        self.press_texture = "assets/images/buttons/button_selected.png"

        super().__init__(width=width, text=text, texture=self.normal_texture, texture_hovered=self.hover_texture, texture_pressed=self.press_texture)

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        window = arcade.get_window()
        logging.info(f"The {self.name} has been pressed. Current View: {window.current_view.view_name}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def normal_texture(self):
        return self._normal_texture

    @normal_texture.setter
    def normal_texture(self, value: str):
        self._normal_texture = arcade.load_texture(f"{ABSOLUTE_PATH}/{value}")

    @property
    def hover_texture(self):
        return self._hover_texture

    @hover_texture.setter
    def hover_texture(self, value: str):
        self._hover_texture = arcade.load_texture(f"{ABSOLUTE_PATH}/{value}")

    @property
    def press_texture(self):
        return self._press_texture

    @press_texture.setter
    def press_texture(self, value: str):
        self._press_texture = arcade.load_texture(f"{ABSOLUTE_PATH}/{value}")
