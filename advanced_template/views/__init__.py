"""
This allows me to import from the views folder instead of importing from the selected file.
Used to be: from advanced_template.views.[Filename] import [Viewname]
Now is    : from advanced_template.views import [Viewname}
"""

from .base_view import BaseView
from .main_menu_view import MainMenuView
