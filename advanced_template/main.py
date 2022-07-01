import arcade, logging

from advanced_template.views import MainMenuView



class GameWindow(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        """
        This is the main window which all things will run on.

        :param width: Width of the Screen
        :param height: Height of the Screen
        :param title: Title of the Screen
        """
        logging.info("Initialisation of the game window has started ")
        super().__init__(width=width, height=height, title=title, resizable=False)

        self.views = {}
        self.views["main_menu"] = MainMenuView()

        logging.info("Initialisation of the game window has been completed")


def pre_window_setup():
    """
    This should run before the window is created
    """

    # Logging system
    level = logging.INFO  # Debug level will fill the file with thousands of:
    # [application.py:668 flip()] Garbage collected 0 OpenGL resource(s)
    format = '%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d %(funcName)s()] %(message)s'
    logging.basicConfig(format=format,
                        datefmt='%H:%M:%S',
                        level=level,
                        filename="log_file.txt",
                        filemode="w")
    logging.info("Logging system has been set up")

    if arcade.VERSION != "2.6.15":
        logging.warning(f"This was developed using Arcade 2.6.15, but your current version is {arcade.VERSION}. "
                        f"The game might not work")


def window_setup():
    """
    This setups the arcade window
    """

    pre_window_setup()
    window = GameWindow(1000, 1000, "Advanced Arcade Template")
    window.show_view(window.views["main_menu"])
    logging.info("Running the Window")
    arcade.run()


def main():
    """
    This function is used to call the other necessary functions to start the game.
    """
    window_setup()

# This runs the program only when the file is directly run.
if __name__ == "__main__":
    main()
