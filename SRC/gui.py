import os
import gettext
from PySide6.QtWidgets import (QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMenuBar)
from PySide6.QtGui import QAction
from SRC.parser import parse_xliff

_ = gettext.gettext  # Translation shortcut

# Initialize gettext for translations
gettext.bindtextdomain("messages", "SRC/translations")
gettext.textdomain("messages")
_ = gettext.gettext  # Now _ is assigned correctly

class XLIFFValidatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(_("XLIFF Validator"))
        self.setGeometry(100, 100, 600, 400)

        # Create menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu(_("File"))

        open_action = QAction(_("Open XLIFF"), self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        exit_action = QAction(_("Exit"), self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Table to display extracted data
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels([_("Segment ID"), _("Source"), _("Target")])

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        """ Open an XLIFF file using a file dialog """
        file_path, _ = QFileDialog.getOpenFileName(self, _("Open XLIFF File"), "", _("XLIFF Files (*.xliff *.sdlxliff)"))
        if file_path:
            self.load_xliff(file_path)
        else:
            QMessageBox.warning(self, _("No File Selected"), _("You must select a valid XLIFF file."))

    def load_xliff(self, file_path):
        """ Load and display XLIFF content in table format """
        segments = parse_xliff(file_path)
        self.table.setRowCount(len(segments))

        for row, (seg_id, source, target, error) in enumerate(segments):
            self.table.setItem(row, 0, QTableWidgetItem(seg_id))
            self.table.setItem(row, 1, QTableWidgetItem(source))
            self.table.setItem(row, 2, QTableWidgetItem(target))
            if error:
                self.table.item(row, 2).setBackground("#FFCCCC")  # Highlight errors
