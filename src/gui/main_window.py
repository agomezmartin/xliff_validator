from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from src.gui.home_screen import HomeScreen
from src.gui.validator_screen import ValidatorScreen
from src.gui.language_selector import LanguageSelector
import gettext

_ = gettext.gettext  # Get translated text

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(_("XLIFF Validator"))

        # ✅ Start with auto-sized Home Screen
        self.home_screen = HomeScreen(self)
        self.language_selector = LanguageSelector(self)
        self.validator_screen = ValidatorScreen(self)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.home_screen)
        self.stack.addWidget(self.language_selector)
        self.stack.addWidget(self.validator_screen)
        self.setCentralWidget(self.stack)

        self.create_menu()

        self.adjustSize()  # ✅ Auto-size initially

    def create_menu(self):
        """Creates a top menu bar with navigation options."""
        menubar = self.menuBar()
        file_menu = menubar.addMenu(_("File"))

        # Feature Selection Actions
        validate_action = QAction(_("Validate XLIFF"), self)
        validate_action.triggered.connect(lambda: self.open_feature_screen(self.validator_screen, large=True))

        lang_action = QAction(_("Change Language"), self)
        lang_action.triggered.connect(lambda: self.open_feature_screen(self.language_selector, large=False))

        exit_action = QAction(_("Exit"), self)
        exit_action.triggered.connect(self.close_application)

        file_menu.addAction(validate_action)
        file_menu.addAction(lang_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

    def open_feature_screen(self, screen, large=True):
        """Switch screens with fade-in effect."""
        self.fade_out_animation(lambda: self._switch_screen(screen, large))

    def _switch_screen(self, screen, large):
        """Switches to a feature screen and adjusts window size."""
        self.stack.setCurrentWidget(screen)
        
        if large:
            self.resize(900, 600)  # ✅ Expand for Validator Screen
        else:
            self.adjustSize()  # ✅ Auto-size smaller screens

        self.fade_in_animation()

    def go_home(self):
        """Navigate back to the home screen with animation."""
        self.fade_out_animation(lambda: self._switch_screen(self.home_screen, large=False))

    def fade_out_animation(self, callback):
        """Fades out the current screen before switching."""
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)  # ✅ 300ms fade-out
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.finished.connect(callback)
        self.animation.start()

    def fade_in_animation(self):
        """Fades in the new screen after switching."""
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(300)  # ✅ 300ms fade-in
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.InCubic)
        self.animation.start()

    def close_application(self):
        """Closes the application with fade-out effect."""
        self.fade_out_animation(self.close)
