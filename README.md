# QA Report Generator

The tool enables XLIFF file validation and produces a QA Report for all segments in the file.
The following information is produced:

- Segment ID
- Source
- Target
- QA Status:
	1. Correct
	2. Untranslated Segment
	3. Mismatch/missing tag

Report can be exported to Excel (.xlsx) file.

The application has been internationalized. Currently available in English, Spanish and a French pseudo-translation.

## i18n Project Structure (internationalization)
```
xliff_validator/
│── locale/
│   ├── messages.pot			(Main source English file)
│   ├── es/
│   │   ├── LC_MESSAGES/
│   │   │   ├── messages.po		(Translated language-specific file)
│   │   │   ├── messages.mo		(Binary language-specific file)
│── src/
│   ├── utils/
│   │   ├── i18n.py			(Sets language)
│── XLIFF_validator.py
```
## Important Notes
- Ensure that `messages.mo` exists under `locale/es/LC_MESSAGES/`. This compiled translation file is necessary for proper localization.

## Usage
To run the validator, execute the main script:
```bash
python XLIFF_validator.py
```

## Full project folder structure
```
xliff_validator/
│── locale/
│   ├── messages.pot         (Main source English file)
│   ├── es/
│   │   ├── LC_MESSAGES/
│   │   │   ├── messages.po  (Translated language-specific file)
│   │   │   ├── messages.mo  (Binary language-specific file)
│   ├── en/
│   │   ├── LC_MESSAGES/
│   │   │   ├── messages.po
│   │   │   ├── messages.mo
│   ├── fr/
│   │   ├── LC_MESSAGES/
│   │   │   ├── messages.po  (Translated language-specific file for French)
│   │   │   ├── messages.mo  (Binary language-specific file for French)
│── src/
│   ├── gui/
│   │   ├── main_window.py    (Main UI window)
│   │   ├── home_screen.py    (Home screen UI)
│   │   ├── validator_screen.py (Validation results screen)
│   │   ├── file_handler.py   (Handles file selection)
│   ├── logic/
│   │   ├── qa_checker.py     (Validates XLIFF segments)
│   │   ├── xliff_parser.py   (Parses XLIFF files and extracts segments)
│   │   ├── excel_exporter.py (Exports validation results to Excel)
│   │   ├── database_exporter.py (Sends validation results to Database. Currently deactivated)
│   ├── utils/
│   │   ├── i18n.py           (Handles internationalization, imports `localedir` from `compiler.py`)
│   │   ├── compiler.py       (Determines the correct locale directory for translations)
│── logs/		      (Logs user activity and errors)
│── XLIFF_validator.py        (Entry point of the application)
```
## Compilation folder structure
```
│── dist/                     (Final executable output from PyInstaller)
│   ├── XLIFF_validator/      (Contains extracted files when running in standard mode)
│   │   ├── _internal/
│   │   │   ├── locale/       (Holds compiled `.mo` translation files)
│   │   ├── XLIFF_validator.exe (Executable file)
```

## License
This project is licensed under [MIT License](./LICENSE.txt).

