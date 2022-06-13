import arcade, logging


class GameWindow(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        """
        This is the main window which all things will run on.

        :param width: Width of the Screen
        :param height: Height of the Screen
        :param title: Title of the Screen
        """
        logging.debug("Initialisation of the game window has started ")
        super().__init__(width=width, height=height, title=title, resizable=False)

        logging.debug("Initialisation of the game window has been completed")

    def setup(self):
        """
        This will be run to setup the window. Can be called again to restart the program, if implemented correctly.
        """
        logging.debug("Setup of the game window has started")

        # Set the colour of the window (arcade uses color not colour!)
        arcade.set_background_color(arcade.color.BLUEBERRY)

        logging.debug("Setup of the game window has been completed")

    def on_draw(self):
        """
        This runs every frame to draw stuff to the window.
        """

        # This starts drawing, avoid calling finish_render()!
        arcade.start_render()



def pre_window_setup():
    """
    This should run before the window is created
    """

    # Logging system
    level = logging.DEBUG
    format = '%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d %(funcName)s()] %(message)s'
    logging.basicConfig(format=format,
                        datefmt='%H:%M:%S',
                        level=level,
                        filename="log_file.txt",
                        filemode="w")
    logging.debug("Logging system has been set up")

    if arcade.VERSION != "2.6.15":
        logging.warning(f"This was developed using Arcade 2.6.15, but your current version is {arcade.VERSION}. "
                        f"The game might not work")


def window_setup():
    """
    This setups the arcade window
    """
    window = GameWindow(1000, 1000, "Advanced Arcade Template")
    window.setup()
    logging.debug("Running the Window")
    arcade.run()


def main():
    """
    This function is used to call the other necessary functions to start the game.
    """
    pre_window_setup()
    window_setup()


# This runs the program only when the file is directly run.
if __name__ == "__main__":
    main()
