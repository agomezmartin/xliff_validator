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
│   │   ├── i18n.py			(Set language)
│── XLIFF_validator.py
```
## Important Notes
- Ensure that `messages.mo` exists under `locale/es/LC_MESSAGES/`. This compiled translation file is necessary for proper localization.

## Usage
To run the validator, execute the main script:
```bash
python XLIFF_validator.py
```

## Full project

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
│── src/
│   ├── gui/
│   │   ├── main_window.py    (Main UI window)
│   │   ├── home_screen.py    (Home screen UI)
│   │   ├── validator_screen.py (Validation results screen)
│   │   ├── file_handler.py   (Handles file selection)
│   ├── logic/
│   │   ├── qa_checker.py     (Validates XLIFF segments)
│   │   ├── excel_exporter.py (Exports validation results to Excel)
│   ├── utils/
│   │   ├── i18n.py           (Handles internationalization, imports `localedir` from `compiler.py`)
│   │   ├── compiler.py       (Determines the correct locale directory for translations)
│── XLIFF_validator.py        (Entry point of the application)

│── dist/                     (Final executable output from PyInstaller)
│   ├── XLIFF_validator/      (Contains extracted files when running in standard mode)
│   │   ├── _internal/
│   │   │   ├── locale/       (Holds compiled `.mo` translation files)
│   │   ├── XLIFF_validator.exe (Executable file)
```
## License
This project is licensed under [MIT License](LICENSE).
