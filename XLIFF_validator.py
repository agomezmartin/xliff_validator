import sys
import gettext
from PySide6.QtWidgets import QApplication
from src.gui.main_window import MainWindow
from src.utils.i18n import gettext_gettext  # ✅ Import translation from separate module

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
