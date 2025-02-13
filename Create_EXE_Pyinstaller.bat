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
REM --add-data "locale;local": this parameter imports l10n files into the executable
REM pyinstaller XLIFF_validator.spec --noconfirm
REM pyinstaller --add-data "locale;locale" --noconsole --icon=c:\xliff_validator\src\resources\executable.ico XLIFF_validator.py
pyinstaller --add-data "locale;locale" --onefile --noconsole --icon=c:\xliff_validator\src\resources\executable.ico XLIFF_validator.py


echo Build complete!















color 0A
echo ===========================================================================
echo File "XLIFF_validator.py" has been compiled to .exe
echo ===========================================================================

pause
