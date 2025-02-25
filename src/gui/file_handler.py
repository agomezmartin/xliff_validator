from PySide6.QtWidgets import QFileDialog, QMessageBox
import os
from src.utils.logs_config import logging
from src.utils.i18n import gettext_gettext  # ✅ Import translation

def select_file():
    """
    Opens a file dialog for the user to select an XLIFF file.
    Ensures the selected file exists and is a valid XLIFF format.
    Returns the file path if valid; otherwise, returns None.
    """
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        gettext_gettext("Select an XLIFF File"),
        "",
        gettext_gettext("XLIFF Files (*.xlf *.xliff);;All Files (*)")
    )

    if not file_path:  # User canceled the dialog
        return None

    # Validate if the file actually exists
    if not os.path.exists(file_path):
        show_error(gettext_gettext("Error"), gettext_gettext("The selected file does not exist."))
        logging.error(gettext_gettext("The selected file does not exist."))
        return None

    # Validate file extension
    if not file_path.lower().endswith(('.xlf', '.xliff')):
        show_error(gettext_gettext("Invalid File"), gettext_gettext("Please select a valid XLIFF file (.xlf or .xliff)."))
        return None

    return file_path

def show_error(title, message):
    """
    Displays an error message box with the given title and message.
    """
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()
