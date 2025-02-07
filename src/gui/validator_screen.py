from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTableWidget, QTableWidgetItem
import os
from src.logic.xliff_parser import parse_xliff
from src.logic.qa_checker import check_segments
import gettext

_ = gettext.gettext  # Get translated text

class ValidatorScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()

        self.label = QLabel(_("Select an XLIFF file to validate"))
        layout.addWidget(self.label)

        self.file_btn = QPushButton(_("Open File"))
        self.file_btn.clicked.connect(self.load_file)  # Connect button to function
        layout.addWidget(self.file_btn)

        self.results_table = QTableWidget(0, 4)
        self.results_table.setHorizontalHeaderLabels([_("Segment ID"), _("Source"), _("Target"), _("QA Status")])
        layout.addWidget(self.results_table)

        back_btn = QPushButton(_("Back to Home"))
        back_btn.clicked.connect(self.main_window.go_home)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def load_file(self):
        """Opens a file dialog, loads an XLIFF file, and displays QA results."""
        file_path, _ = QFileDialog.getOpenFileName(self, _("Open XLIFF File"), "", "XLIFF Files (*.xliff *.sdlxliff);;All Files (*)")

        if not file_path:  # If user cancels, do nothing
            return

        if not os.path.exists(file_path):  # Check if the file path is valid
            self.label.setText(_("Error: File not found!"))
            return

        try:
            segments = parse_xliff(file_path)  # Extract XLIFF content
            qa_results = check_segments(segments)  # Run QA checks
            self.populate_results(qa_results)  # Show results in table
        except Exception as e:
            self.label.setText(_("Error loading file: ") + str(e))

    def populate_results(self, results):
        """Displays the extracted segments and QA results in a table."""
        self.results_table.setRowCount(len(results))
        
        for row, (seg_id, source, target, status) in enumerate(results):
            self.results_table.setItem(row, 0, QTableWidgetItem(str(seg_id)))
            self.results_table.setItem(row, 1, QTableWidgetItem(source))
            self.results_table.setItem(row, 2, QTableWidgetItem(target))

            item = QTableWidgetItem(status)
            if "ERROR" in status:
                item.setBackground("red")  # Highlight errors in red
            elif "Correct" in status:
                item.setBackground("green")  # Highlight correct entries in green

            self.results_table.setItem(row, 3, item)
