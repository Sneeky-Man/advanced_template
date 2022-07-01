# Changelog

### This is a detailed list of all the changes made to the template.
#### I use this since I like only making a commit or two a day, but I still want to catalog all I have done.


#### 13/06/22, 16:50
* Initial commit of most files

#### 13/06/22, 17:33
* Fixed typo in `README.md`
* Updated `CHANGELOG.md` description 
* Added logging system
* Added the beginning of the `GameWindow`

#### 21/06/22, 16:50
* Added `CREDITS.md`. This is where I credit people whose code I have ~~stolen~~ used.
* Changed it from a window only version to a view based version. Code taken from the [community platformer](https://github.com/pythonarcade/community-platformer).
* Added `__init__.py`, `base_view.py` and `main_menu_view.py` to the new views folder.
* Removed a lot of code from `GameWindow`, and moved it to the new views.
* Changed the logging system level from debug to info. This was because debug was being spammed with useless info.
* Added `this effect` to all files, classes, and variables in `CHANGELOG.md`.


#### 01/07/22, 19:00
* Added `__init__.py`, `buttons.py` to the new special_scripts.
* Added `BasicButton` to `buttons.py`.
* Added three buttons assets.
* Added `path.py`. This is used to find the absolute path.
* Updated `CREDITS.md`.
* Added automatic logging to the on_click event for the `BasicButton`.
* Added a start, settings and quit buttons to the `MainMenuView`. Currently, only the quit button works as intended.