from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QStackedWidget
from PySide6.QtGui import QAction
from src.gui.home_screen import HomeScreen
from src.gui.validator_screen import ValidatorScreen
from PySide6.QtCore import Qt
from src.utils.i18n import gettext_gettext  # ✅ Import translation

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle(gettext_gettext("XLIFF Validator"))
        self.setGeometry(100, 100, 800, 600)

        # Set up central widget
        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create screens
        self.home_screen = HomeScreen(self)
        self.validator_screen = ValidatorScreen(self)

        # Add screens to the central widget
        self.central_widget.addWidget(self.home_screen)
        self.central_widget.addWidget(self.validator_screen)

        # Create top-level menu
        self.create_menu()

    def create_menu(self):
        """ ✅ Creates the top-level menu with a File dropdown. """
        menu_bar = self.menuBar()

        # ✅ Create "File" Menu
        file_menu = QMenu(gettext_gettext("File"), self)
        menu_bar.addMenu(file_menu)

        # ✅ "Validate XLIFF File" Action (Now just navigates to validator screen)
        validate_action = QAction(gettext_gettext("Validate XLIFF File"), self)
        validate_action.triggered.connect(self.show_validator_screen)
        file_menu.addAction(validate_action)

        # ✅ "Exit" Action
        exit_action = QAction(gettext_gettext("Exit"), self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def show_validator_screen(self):
        """ ✅ Shows the Validator Screen (does not auto-open file dialog). """
        self.central_widget.setCurrentWidget(self.validator_screen)

    def show_home_screen(self):
        """ ✅ Navigates back to the Home Screen. """
        self.central_widget.setCurrentWidget(self.home_screen)
