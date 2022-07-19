# I changed the naming since i felt the community platformer's names were a bit confusing, especially to new
# programmers to arcade

import arcade
import arcade.gui
import logging

"""
Plan of how the view should work.

Before the view needs to be used:
It should be initialised to the views list. This will only do what is in the init, which isn't much

When the view needs to be used:
setup will be run before the view is shown. This will have to be done manually

on_show_view will be run automatically due to arcade. However, it cannot, to my knowledge, take variables, and so
should only be used when the view is ready to be shown
"""

class BaseView(arcade.View):
    def __init__(self, view_name: str):
        """
        This is the base view, which all other views will be based off.

        :param view_name: The name of the view.
        """
        logging.info(f"Initialisation of the {view_name} view has started")
        super().__init__()
        self.view_name = view_name
        self.ui_manager = arcade.gui.UIManager()

        logging.info(f"Initialisation of the {view_name} view has been completed")

    def setup(self):
        """
        This will be MANUALLY run before the view is shown to setup the view. Re-Run this to reset the view.
        The only exception is if you have already setup the view, and want to switch back to where it was
        (Like if your in settings and you want to go back to the game, don't run this).
        """
        logging.info(f"Setup of the {self.view_name} view has started")

        logging.info(f"Setup of the {self.view_name} view has been completed")

    def on_show_view(self):
        """
        This will ALWAYS be run when the view is shown.
        This CANNOT take variables, and so will only be used when the view is completely ready to be shown.
        It will largely be used for logging purposes, and enabling the ui_manager.
        """
        logging.info(f"Show View of the {self.view_name} has started")
        super().on_show_view()
        self.ui_manager.enable()

        logging.info(f"Show View of the {self.view_name} has been completed")

    def on_hide_view(self):
        """
        This will ALWAYS be run when the view has stopped being shown.
        It will largely be used for logging purposes, and disabling the ui_manager.
        """
        logging.info(f"Hide View of the {self.view_name} has started")
        super().on_hide_view()
        self.ui_manager.disable()
        logging.info(f"Hide View of the {self.view_name} has been completed")


    def changing_view_with_key(self, key: int, modifiers: int, current_view_name, new_view_name):
        """
        This will be used when changing to a new view using a key. Purely for logging purposes.
        """
        logging.info(f"The key {key} has been pressed. Current View: {current_view_name}. New View: {new_view_name}")

    def changing_view_with_button(self):
        """
        This will be used when changing to a new view using a button. Purely for logging purposes.
        """
        logging.info(f"Not added yet")
        ## TODO Implement this

    """
   @property is a getter/setter. Its really just another way of doing self.started = started.
   I just want to get into the habit of doing this, as i can do a lot of helpful stuff with it later on.
   Also, remember to do return and assigning the value with a _. Failing to do so will produce a recursive error.
    """
    @property
    def view_name(self):
        return self._view_name

    @view_name.setter
    def view_name(self, value: str):
        self._view_name = value

    @property
    def ui_manager(self):
        return self._ui_manager

    @ui_manager.setter
    def ui_manager(self, value):
        self._ui_manager = value

"""
class BlueprintView(BaseView):
    def __init__(self):
        """"""
        This is a blueprint for future views
        """"""
        super().__init__(view_name="blueprint")
        
    def setup(self):
        super().setup()
    
    def on_show_view(self):
        super().on_show_view()
    
    def on_hide_view(self):
        super().on_hide_view()
    
    def on_draw(self):
        arcade.start_render()
        self.clear()
        self.ui_manager.draw()
        """
