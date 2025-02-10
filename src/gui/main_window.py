from PySide6.QtWidgets import QMainWindow, QStackedWidget, QMenuBar
from PySide6.QtGui import QAction
from src.gui.home_screen import HomeScreen
from src.gui.validator_screen import ValidatorScreen
import gettext

gettext.bindtextdomain("messages", "locale")
gettext.textdomain("messages")
translation = gettext.translation("messages", "locale", fallback=True)
gettext_gettext = translation.gettext

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("XLIFF Validator")
        self.setGeometry(100, 100, 800, 600)

        # Create stacked widget for screen switching
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Instantiate screens
        self.home_screen = HomeScreen(self)
        self.validator_screen = ValidatorScreen(self)

        # Add screens to stacked widget
        self.central_widget.addWidget(self.home_screen)
        self.central_widget.addWidget(self.validator_screen)

        # Set up the top-level menu
        self.create_menu()

        # Show the home screen initially
        self.show_home_screen()

    def create_menu(self):
        """✅ Creates the top-level menu."""
        menu_bar = self.menuBar()

        # Language Menu
        language_menu = menu_bar.addMenu(gettext_gettext("Language"))
        change_language_action = QAction(gettext_gettext("Change Language"), self)
        change_language_action.triggered.connect(self.show_language_selector)
        language_menu.addAction(change_language_action)

        # Exit Menu
        exit_menu = menu_bar.addMenu(gettext_gettext("Exit"))
        exit_action = QAction(gettext_gettext("Exit Application"), self)
        exit_action.triggered.connect(self.close)
        exit_menu.addAction(exit_action)

    def show_home_screen(self):
        """ ✅ Show Home Screen """
        self.resize(600, 400)  # Make Home Screen smaller
        self.central_widget.setCurrentWidget(self.home_screen)

    def open_feature_screen(self, screen, large=False):
        """ ✅ Show the requested feature screen """
        if large:
            self.resize(1024, 768)  # Switch to larger mode
        else:
            self.resize(800, 600)  # Default size
        self.central_widget.setCurrentWidget(screen)

    def show_language_selector(self):
        """ ✅ Placeholder for language selector functionality. """
        print("Language selector not yet implemented.")
