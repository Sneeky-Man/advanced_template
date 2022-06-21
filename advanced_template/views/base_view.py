# I changed the naming since i felt the community platformer's names were a bit confusing, especially to new
# programmers like i once was.

from arcade import View
import logging


class BaseView(View):
    def __init__(self, view_name):
        """
        This is what all views will be based off.
        """
        logging.info(f"Initialisation of the {view_name} view has started")
        super().__init__()

        self.view_name = view_name
        self.started = False
        self.ui_manager = None
        logging.info(f"Initialisation of the {view_name} view has been completed")

    def setup(self):
        """
        Sets up the view
        """
        logging.info(f"Setup of the {self.view_name} view has started")

        self.started = True

        logging.info(f"Setup of the {self.view_name} view has been completed")

    def on_show(self):
        """
        When the view is shown, it enabled ui manager and called the setup if a setup has not been done yet.
        """
        if not self.started:
            self.setup()

        if self.ui_manager:
            self.ui_manager.enable()

    def on_hide_view(self):
        """
        When the view is hidden, it disables the ui manager.
        """
        if self.ui_manager:
            self.ui_manager.disable()

    """
    @property is a getter/setter. Its really just another way of doing self.started = started. 
    I just want to get into the habit of doing this, as i can do a lot of helpful stuff with it later on.
    Also, remember to do return and assigning the value with a _. Failing to do so will produce a recursive error.
    """

    @property
    def started(self):  # Used to track if a view has been ran it's setup function or not
        return self._started

    @started.setter
    def started(self, value: bool):
        self._started = value

    @property
    def ui_manager(self):  # The views UI manager, this is optional for a view to use
        return self._ui_manager

    @ui_manager.setter
    def ui_manager(self, value):
        self._ui_manager = value

    @property
    def view_name(self): # Used for logging purposes
        return self._view_name

    @view_name.setter
    def view_name(self, value: str):
        self._view_name = value
