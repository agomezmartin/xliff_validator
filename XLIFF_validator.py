import sys
import gettext
from PySide6.QtWidgets import QApplication
from SRC.gui import XLIFFValidatorGUI

# Internationalization setup
gettext.bindtextdomain("messages", "SRC/translations")
gettext.textdomain("messages")
_ = gettext.gettext  # Shortcut for translations

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = XLIFFValidatorGUI()
    window.show()
    sys.exit(app.exec())
