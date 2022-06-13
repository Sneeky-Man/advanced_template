import arcade


def pre_window_setup():
    """
    This should run before the window is created
    """
    if arcade.VERSION != "2.6.15":
        print(f"Warning. This was developed using Arcade 2.6.15, but your current version is {arcade.VERSION}."
              f"The game might not work")


def main():
    """
    This function is used to call the other necessary functions to start the game.
    """
    pre_window_setup()


# This runs the program only when the file is directly run.
if __name__ == "__main__":
    main()
