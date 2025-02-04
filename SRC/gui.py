import os
import gettext
from PySide6.QtWidgets import (
    QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMenuBar, QMessageBox, QStackedWidget, QLabel, QPushButton
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from SRC.parser import parse_xliff

# Initialize gettext for translations
gettext.bindtextdomain("messages", "SRC/translations")
gettext.textdomain("messages")
_ = gettext.gettext  # Shortcut for translations

class XLIFFValidatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(gettext.gettext("XLIFF Validator"))
        self.setGeometry(100, 100, 700, 400)

        # Create menu bar
        self.create_menu_bar()

        # Create central widget stack (to switch screens)
        self.central_stack = QStackedWidget()
        self.setCentralWidget(self.central_stack)

        # Create screens
        self.welcome_screen = self.create_welcome_screen()
        self.validator_screen = self.create_validator_screen()

        # Add screens to stack
        self.central_stack.addWidget(self.welcome_screen)
        self.central_stack.addWidget(self.validator_screen)

    def create_menu_bar(self):
        """Creates the top-level menu bar."""
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu(gettext.gettext("File"))

        open_action = QAction(gettext.gettext("Open XLIFF File"), self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        exit_action = QAction(gettext.gettext("Exit"), self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Help Menu
        help_menu = menu_bar.addMenu(gettext.gettext("Help"))

        about_action = QAction(gettext.gettext("About"), self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

    def create_welcome_screen(self):
        """Creates the welcome screen with a centered title and open file button."""
        screen = QWidget()
        layout = QVBoxLayout()

        # Centered Title
        welcome_label = QLabel(gettext.gettext("Welcome to XLIFF Validator"))
        welcome_label.setAlignment(Qt.AlignCenter)  # Center-align the text
        welcome_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(welcome_label)

        open_file_btn = QPushButton(gettext.gettext("Open XLIFF File"))
        open_file_btn.clicked.connect(self.open_file)
        layout.addWidget(open_file_btn)

        screen.setLayout(layout)
        return screen

    def create_validator_screen(self):
        """Creates the main validator screen with table and back button."""
        screen = QWidget()
        layout = QVBoxLayout()

        # Table to display extracted data
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            gettext.gettext("Segment ID"), gettext.gettext("Source"), gettext.gettext("Target"), gettext.gettext("QA Status")
        ])
        layout.addWidget(self.table)

        # Back button to return to home screen
        back_button = QPushButton(gettext.gettext("Back to Home Screen"))
        back_button.clicked.connect(self.show_welcome_screen)
        layout.addWidget(back_button)

        screen.setLayout(layout)
        return screen

    def open_file(self):
        """Opens an XLIFF file using a file dialog."""
        file_path, _ = QFileDialog.getOpenFileName(self, gettext.gettext("Open XLIFF File"), "", gettext.gettext("XLIFF Files (*.xliff *.sdlxliff)"))
        if file_path:
            self.load_xliff(file_path)
            self.central_stack.setCurrentWidget(self.validator_screen)
        else:
            QMessageBox.warning(self, gettext.gettext("No File Selected"), gettext.gettext("You must select a valid XLIFF file."))

    def load_xliff(self, file_path):
        """Loads and displays XLIFF content in table format with QA Status."""
        segments = parse_xliff(file_path)
        self.table.setRowCount(len(segments))

        for row, (seg_id, source, target, error) in enumerate(segments):
            self.table.setItem(row, 0, QTableWidgetItem(seg_id))
            self.table.setItem(row, 1, QTableWidgetItem(source))
            self.table.setItem(row, 2, QTableWidgetItem(target))
            self.table.setItem(row, 3, QTableWidgetItem(error or gettext.gettext("No Issues")))

            if error:
                self.table.item(row, 3).setBackground("#FFCCCC")  # Highlight errors

    def show_welcome_screen(self):
        """Switches back to the welcome screen."""
        self.central_stack.setCurrentWidget(self.welcome_screen)

    def show_about_dialog(self):
        """Displays an About dialog."""
        QMessageBox.information(self, gettext.gettext("About"), gettext.gettext("XLIFF Validator\nVersion 1.0\n2025"))
