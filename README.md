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
│── XLIFF_validator.py
```
## Important Notes
- Ensure that `messages.mo` exists under `locale/es/LC_MESSAGES/`. This compiled translation file is necessary for proper localization.

## Usage
To run the validator, execute the main script:
```bash
python XLIFF_validator.py
```

## License
This project is licensed under [MIT License](LICENSE).

