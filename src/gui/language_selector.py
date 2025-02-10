from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import os
import gettext

_ = gettext.gettext

# Supported languages
LANGUAGES = {
    "English": "en",
    "French": "fr",
    "Spanish": "es"
}

class LanguageSelector(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        font = QFont("Quicksand", 14)  # ✅ Now using built-in QFont

        # Language Selection Label
        self.label = QLabel(gettext.gettext("Select Language"))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Language Dropdown
        self.language_dropdown = QComboBox()
        self.language_dropdown.setFont(font)
        self.language_dropdown.addItems(LANGUAGES.keys())

        # ✅ Center dropdown
        dropdown_layout = QHBoxLayout()
        dropdown_layout.addStretch()
        dropdown_layout.addWidget(self.language_dropdown)
        dropdown_layout.addStretch()
        layout.addLayout(dropdown_layout)

        # Apply Button
        self.apply_button = QPushButton(gettext.gettext("Apply"))
        self.apply_button.setFont(font)
        self.apply_button.setStyleSheet(self.get_button_style())  # ✅ Fixed

        # Back to Home Button
        self.back_button = QPushButton(gettext.gettext("Back to Home"))
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(self.get_button_style())  # ✅ Fixed
        self.back_button.clicked.connect(self.main_window.go_home)

        # ✅ Center buttons
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.apply_button)
        btn_layout.addWidget(self.back_button)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.adjustSize()

    def get_button_style(self):
        """✅ Fixed: Returns button styling (Previously missing)."""
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

