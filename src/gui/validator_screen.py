from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from src.logic.qa_checker import parse_xliff
from src.logic.excel_exporter import export_to_excel
import gettext

# Initialize gettext for translations
gettext.bindtextdomain("messages", "locale")
gettext.textdomain("messages")
translation = gettext.translation("messages", "locale", fallback=True)
gettext_gettext = translation.gettext

class ValidatorScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.results = []

        self.init_ui()

    def init_ui(self):
        """ ✅ Sets up the Validator UI. """
        layout = QVBoxLayout()

        # ✅ "Open XLIFF File" Button
        open_xliff_btn = QPushButton(gettext_gettext("Open XLIFF File"))
        open_xliff_btn.setStyleSheet("padding: 8px; font-size: 14px;")
        open_xliff_btn.clicked.connect(self.handle_file_selection)
        layout.addWidget(open_xliff_btn)

        # ✅ Title Label
        self.title_label = QLabel(gettext_gettext("XLIFF Validation Report"))
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(self.title_label)

        # ✅ Table for displaying results
        self.table = QTableWidget()
        layout.addWidget(self.table)

        # ✅ Export Button
        self.export_button = QPushButton(gettext_gettext("Export to Excel"))
        self.export_button.setStyleSheet("padding: 8px; font-size: 14px;")
        self.export_button.clicked.connect(self.export_results)
        layout.addWidget(self.export_button)

        # ✅ Back to Home Button
        self.back_home_btn = QPushButton(gettext_gettext("Back to Home"))
        self.back_home_btn.setStyleSheet("padding: 8px; font-size: 14px;")
        self.back_home_btn.clicked.connect(self.main_window.show_home_screen)
        layout.addWidget(self.back_home_btn)

        self.setLayout(layout)

    def handle_file_selection(self):
        """ ✅ Prompts user to open an XLIFF file and triggers validation. """
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter(gettext_gettext("XLIFF Files (*.xliff *.xml)"))  # Corrected method to set file filter
        file_dialog.setViewMode(QFileDialog.List)

        # ✅ Open file dialog and get selected file
        file_path, _ = file_dialog.getOpenFileName(self, gettext_gettext("Open XLIFF File"))
        if file_path:
            self.handle_file_validation(file_path)  # Trigger validation for the selected file
        else:
            print(gettext_gettext("No file selected."))

    def handle_file_validation(self, file_path):
        """ ✅ Validates the selected XLIFF file and displays the results. """
        results = parse_xliff(file_path)
        self.show_results(results)

    def show_results(self, results):
        """ ✅ Displays validation results in a table. """
        self.results = results
        self.table.setRowCount(len(results))
        self.table.setColumnCount(4)  # Segment ID, Source, Target, QA Status
        self.table.setHorizontalHeaderLabels([
            gettext_gettext("Segment ID"),
            gettext_gettext("Source"),
            gettext_gettext("Target"),
            gettext_gettext("QA Status")
        ])

        # ✅ Set table properties for better UI
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for row, (segment_id, source, target, qa_status) in enumerate(results):
            self.table.setItem(row, 0, QTableWidgetItem(segment_id))
            self.table.setItem(row, 1, QTableWidgetItem(source))
            self.table.setItem(row, 2, QTableWidgetItem(target))
            self.table.setItem(row, 3, QTableWidgetItem(qa_status))

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

    def export_results(self):
        """ ✅ Calls the export function to save results to Excel. """
        if self.results:
            export_to_excel(self.results, self)
        else:
            print(gettext_gettext("No validation results to export."))
