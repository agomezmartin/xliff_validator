import sys
import os

# ✅ Determine the correct locale directory (FROM executable OR in development)
if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
    base_path = sys._MEIPASS  # PyInstaller temporary extraction directory
    localedir = os.path.join(base_path, "locale")  # Full path for "--onefile" compilation executable file
#     localedir = os.path.join("_internal", "locale")  # Adjusted path for standard executable file (all files visible)
else:
    # localedir = os.path.join(os.path.dirname(__file__), "locale")  # Full path for development mode
    localedir = os.path.join("locale")  # ✅ Export this variable: Adjusted path for development mode 
