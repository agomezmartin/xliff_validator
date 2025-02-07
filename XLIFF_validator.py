import sys
import gettext
from PySide6.QtWidgets import QApplication
from src.gui.main_window import MainWindow

# Initialize gettext for internationalization
gettext.bindtextdomain("messages", "locale")
gettext.textdomain("messages")
_ = gettext.gettext

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
