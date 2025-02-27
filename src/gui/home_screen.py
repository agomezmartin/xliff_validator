from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from src.gui.file_handler import select_file
from src.logic.parse_xliff import parse_xliff
from src.utils.i18n import gettext_gettext  # ✅ Import translation

class HomeScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()

        # ✅ Apply Lato Font (Size 24)
        font = QFont("Lato", 24, QFont.Light)  # Font size 24, light weight

        # ✅ Welcome Label
        label = QLabel(gettext_gettext("Welcome to XLIFF Validator").upper())
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # ✅ Start Button (Validate XLIFF)
        validate_btn = QPushButton(gettext_gettext("Validate XLIFF"))
        validate_btn.setStyleSheet("padding: 10px; font-size: 14px;")
        validate_btn.clicked.connect(self.show_validator_screen)
        layout.addWidget(validate_btn)

        self.setLayout(layout)

    def show_validator_screen(self):
        """ ✅ Navigates to the Validator screen when 'Validate XLIFF' is clicked. """
        self.main_window.central_widget.setCurrentWidget(self.main_window.validator_screen)
