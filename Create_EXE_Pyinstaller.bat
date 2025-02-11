@echo off
REM This batch file compiles XLIFF_validator.py into a standalone .exe
REM using PyInstaller with the specified options and icon.
color 0B

echo ===========================================================================
echo This batch file compiles XLIFF_Validator into a standalone .exe
echo using PyInstaller with the specified options and icon.
echo ===========================================================================

color 0B
REM pyinstaller --log-level=DEBUG --noconsole --add-data "c:\xliff_validator\src\resources\*;src\img" --icon=c:\xliff_validator\src\resources\executable.png XLIFF_validator.py
REM pyinstaller --onefile --log-level=DEBUG --noconsole --add-data "c:\xliff_validator\src\resources\*;src\img" --icon=c:\xliff_validator\src\resources\executable.png XLIFF_validator.py
REM pyinstaller --onefile --noconsole --add-data "c:\xliff_validator\src\resources\*;src\img" --icon=c:\xliff_validator\src\resources\executable.png XLIFF_validator.py
pyinstaller --onefile --noconsole --icon=c:\xliff_validator\src\resources\executable.png XLIFF_validator.py

color 0A
echo ===========================================================================
echo File "XLIFF_validator.py" has been compiled to .exe
echo ===========================================================================

pause
