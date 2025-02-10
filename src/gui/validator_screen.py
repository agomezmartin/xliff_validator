from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt
from src.gui.file_handler import select_file
from src.logic.qa_checker import parse_xliff
import gettext

gettext.bindtextdomain("messages", "locale")
gettext.textdomain("messages")
translation = gettext.translation("messages", "locale", fallback=True)
gettext_gettext = translation.gettext

class ValidatorScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        # ✅ Apply Quicksand Font
        font = QFont("Quicksand", 18)

        # ✅ Buttons Layout (Top)
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)

        # ✅ Open XLIFF File Button
        open_file_btn = QPushButton(gettext_gettext("Open XLIFF File"))
        open_file_btn.setFont(font)
        open_file_btn.setStyleSheet(self.get_button_style())
        open_file_btn.clicked.connect(self.handle_file_selection)

        # ✅ Spacer to align buttons neatly
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer)

        button_layout.addWidget(open_file_btn)

        # ✅ Back Home Button (Below the QA Report)
        back_home_btn = QPushButton(gettext_gettext("Back to Home"))
        back_home_btn.setFont(font)
        back_home_btn.setStyleSheet(self.get_button_style())
        back_home_btn.clicked.connect(self.main_window.show_home_screen)

        layout.addLayout(button_layout)

        # ✅ Title Label for the Validation Results
        label = QLabel(gettext_gettext("Validation Results"))
        label.setFont(font)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # ✅ Table for QA results
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            gettext_gettext("Segment ID"),
            gettext_gettext("Source"),
            gettext_gettext("Target"),
            gettext_gettext("QA Status"),
        ])
        layout.addWidget(self.table)

        # ✅ Add the "Back Home" button below the table
        back_home_btn_layout = QHBoxLayout()
        back_home_btn_layout.setAlignment(Qt.AlignCenter)
        back_home_btn_layout.addWidget(back_home_btn)

        layout.addLayout(back_home_btn_layout)

        self.setLayout(layout)
        self.adjustSize()

    def handle_file_selection(self):
        """ ✅ Runs validation on real XLIFF files. """
        file_path = select_file()
        if not file_path:
            return
        
        results = parse_xliff(file_path)  # ✅ Process actual XLIFF file
        self.show_results(results)

    def show_results(self, results):
        """ ✅ Display bilingual QA report with color-coded statuses. """
        if isinstance(results, str):  # Handle error messages
            self.table.setRowCount(1)
            self.table.setItem(0, 0, QTableWidgetItem(results))
            return

        self.table.setRowCount(len(results))

        for row, (segment_id, source, target, qa_status) in enumerate(results):
            self.table.setItem(row, 0, QTableWidgetItem(segment_id))
            self.table.setItem(row, 1, QTableWidgetItem(source))
            self.table.setItem(row, 2, QTableWidgetItem(target))

            # ✅ Set QA status with color coding
            status_item = QTableWidgetItem(qa_status)
            status_item.setBackground(self.get_status_color(qa_status))
            self.table.setItem(row, 3, status_item)

    def get_status_color(self, status):
        """ ✅ Returns color for QA status. """
        if gettext_gettext("Correct") in status:
            return QColor(144, 238, 144)  # 🟢 Green
        elif gettext_gettext("Untranslated segment") in status:
            return QColor(255, 255, 102)  # 🟡 Yellow
        elif gettext_gettext("Mismatch/missing tag") in status:
            return QColor(255, 102, 102)  # 🔴 Red
        return QColor(255, 255, 255)  # Default: White

    def get_button_style(self):
        """✅ Returns button styling."""
        return """
        QPushButton {
            background-color: #4CAF50;
            color: white;
            padding: 12px 30px;
            border-radius: 5px;
            font-size: 16px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        """
