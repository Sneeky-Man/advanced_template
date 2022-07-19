from advanced_template.views.base_view import BaseView
from advanced_template.special_scripts import BasicButton
import arcade
import arcade.gui


class MainMenuView(BaseView):
    def __init__(self):
        """
        This is the view for the main menu.
        """
        super().__init__(view_name="main_menu")

    def setup(self):
        super().setup()
        arcade.set_background_color(arcade.color.BLUEBERRY)  # Arcade uses color not colour!)

        self.vertical_box = arcade.gui.UIBoxLayout()

        # Start button
        start_button = BasicButton(name="Start Button", text="START")

        @start_button.event("on_click")
        def on_click_start(event):
            self.window.view_list["game"].setup()
            self.window.show_view(self.window.view_list["game"])

        # Settings Button
        settings_button = BasicButton(name="Settings Button", text="Settings")

        @settings_button.event("on_click")
        def on_click_settings(event):
            self.window.view_list["settings"].setup()
            self.window.show_view(self.window.view_list["settings"])

        # Quit button
        quit_button = BasicButton(name="Quit Button", text="Leave")

        @quit_button.event("on_click")
        def on_click_quit(event):
            arcade.exit()

        self.vertical_box.add(start_button.with_space_around(bottom=20))
        self.vertical_box.add(settings_button.with_space_around(bottom=20))
        self.vertical_box.add(quit_button.with_space_around(bottom=20))
        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.vertical_box))
        self.ui_manager.add(self.vertical_box)

    def on_show_view(self):
        super().on_show_view()

    def on_hide_view(self):
        super().on_hide_view()

    def on_draw(self):
        arcade.start_render()
        self.clear()
        self.ui_manager.draw()

        arcade.draw_text(
            "Advanced Arcade Template",
            self.window.width / 2,
            self.window.height - 125,
            arcade.color.ALLOY_ORANGE,
            font_size=44,
            anchor_x="center",
            anchor_y="center",
        )
        arcade.draw_point(500, 500, arcade.color.PEAR, 20)
