from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtCore import Qt  # ✅ Import for alignment
import gettext
import os

_ = gettext.gettext

class HomeScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # ✅ Center elements

        font = QFont("Quicksand", 14) # ✅ Now using built-in QFont

        # Welcome Label
        label = QLabel(_("Welcome to XLIFF Validator"))
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # Start Button
        validate_btn = QPushButton(_("Start Validation"))
        validate_btn.setFont(font)
        validate_btn.setStyleSheet(self.get_button_style())
        validate_btn.clicked.connect(lambda: self.main_window.open_feature_screen(self.main_window.validator_screen, large=True))

        # ✅ Center button
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(validate_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.adjustSize()  # ✅ Auto-resize to fit content

    def load_quicksand_font(self):
        """Loads the Quicksand font from a local file."""
        font_path = os.path.join(os.path.dirname(__file__), "../resources/Quicksand-Regular.ttf")
        if os.path.exists(font_path):
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id == -1:
                print(_("Error: Failed to load Quicksand font"))

    def get_button_style(self):
        """Returns the stylesheet for buttons."""
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
