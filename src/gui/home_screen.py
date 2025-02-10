from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import gettext

gettext.bindtextdomain("messages", "locale")
gettext.textdomain("messages")
translation = gettext.translation("messages", "locale", fallback=True)
gettext_gettext = translation.gettext

class HomeScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # ✅ Apply Quicksand Font (Size 24)
        font = QFont("Quicksand", 24)

        # ✅ Welcome Label
        label = QLabel(gettext_gettext("Welcome to XLIFF Validator"))
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # ✅ Validate XLIFF Button
        validate_btn = QPushButton(gettext_gettext("Validate XLIFF"))
        validate_btn.setFont(font)
        validate_btn.setStyleSheet(self.get_button_style())
        validate_btn.clicked.connect(self.open_validator_screen)
        layout.addWidget(validate_btn)

        self.setLayout(layout)
        self.adjustSize()

    def open_validator_screen(self):
        """ ✅ Open Validator Screen """
        self.main_window.open_feature_screen(self.main_window.validator_screen, large=True)

    def get_button_style(self):
        """✅ Returns button styling."""
        return """
        QPushButton {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        """
