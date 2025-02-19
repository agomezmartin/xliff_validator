from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QDateTime
from src.logic.qa_checker import parse_xliff
from src.logic.excel_exporter import export_to_excel
from src.logic.database_exporter import export_to_database  # ✅ Import the database exporter
from src.utils.i18n import gettext_gettext  # ✅ Import translation

class ValidatorScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.results = []
        self.file_name = ""  # To store the file name


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

        # ✅ Export to Excel Button
        self.export_excel_button = QPushButton(gettext_gettext("Export to Excel"))
        self.export_excel_button.setStyleSheet("padding: 8px; font-size: 14px;")
        self.export_excel_button.clicked.connect(self.export_to_excel_results)
        self.export_excel_button.setVisible(False)  # Hide 'Export to Excel' button initially
        layout.addWidget(self.export_excel_button)

        # ✅ Export to Database Button
        self.export_db_button = QPushButton(gettext_gettext("Export to Database"))
        self.export_db_button.setStyleSheet("padding: 8px; font-size: 14px;")
        self.export_db_button.clicked.connect(self.export_to_database_results)
        self.export_db_button.setVisible(False)  # Hide 'Export to Database' button initially
        layout.addWidget(self.export_db_button)

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
            self.file_name = file_path.split("/")[-1]  # Extract the file name from the file path
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
        for row in range(self.table.rowCount()):
            status_item = self.table.item(row, 3)
            status_item.setForeground(self.get_status_color(status_item.text()))

        # ✅ Show export buttons after results are displayed
        if results:
            self.export_excel_button.setVisible(True)
            self.export_db_button.setVisible(True)

    def get_status_color(self, status):
            """ ✅ Returns color for QA status (colored text). """
            if gettext_gettext("Correct") in status:
                return QColor(0, 128, 0)  # 🟢 Green for Correct
            elif gettext_gettext("Untranslated segment") in status:
                return QColor(139, 69, 19)  # 🟤 Brown for Untranslated segment
            elif gettext_gettext("Source in target") in status:
                return QColor(139, 69, 19)  # 🟤 Brown for Source in target
            elif gettext_gettext("Source missing") in status:
                return QColor(255, 0, 0)  # 🔴 Red for Source missing
            elif gettext_gettext("Mismatch/missing tag") in status:
                return QColor(255, 0, 0)  # 🔴 Red for Mismatch
            elif gettext_gettext("Pseudotranslated") in status:
                return QColor(0, 0, 255)  # 🔵 Blue for Pseudotranslated
            return QColor(0, 0, 0)  # Default: Black text color for other statuses

    def export_to_excel_results(self):
        """ ✅ Calls the export function to save results to Excel. """
        if self.results:
            export_to_excel(self.results, self)
        else:
            print(gettext_gettext("No validation results to export."))

    def export_to_database_results(self):
        """ ✅ Calls the export function to save results to MySQL database. """
        if self.results:
            file_name = "example_file.xliff"  # Example file name, should be dynamic or passed from handle_file_selection
            current_datetime = QDateTime.currentDateTime() # ✅ Get the current date and time
            date = current_datetime.toString("yyyy-MM-dd HH:mm") # ✅ Format the current datetime as 'yyyy-MM-dd HH:mm'

            if export_to_database(self.results, self.file_name, date): # Pass file name and date to the exporter
                self.show_database_confirmation_message(
                    gettext_gettext("Database confirmation"), # Title
                    gettext_gettext("The QA Report has been added successfully.") # Message
                    )
            else:
              self.show_database_confirmation_message(
                  gettext_gettext("Database confirmation"), # Title
                  gettext_gettext("Error: The report has not been added.") # Message
                  )

        else:
            print(gettext_gettext("No validation results to export."))

    def show_database_confirmation_message(self, title, message):
            """ ✅ Displays a confirmation message box with the given title and message. """
            msg_box = QMessageBox(self)
            if message == gettext_gettext("The QA Report has been added successfully."):
                msg_box.setIcon(QMessageBox.Information)
            else:
                msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle(title)
            msg_box.setText(message)
            msg_box.exec()
