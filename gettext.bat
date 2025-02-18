@echo off
setlocal enabledelayedexpansion

:: Define supported languages (modify as needed)
REM set LANGUAGES=fr de es it
set LANGUAGES=es fr

:: Ensure "locale" directory exists
if not exist locale mkdir locale

:: Create or clear files.txt
echo. > files.txt

@echo ========================================================================
@echo Files to be analyzed for text extraction:
@echo ------------------------------------------------------------------------

:: Loop through all Python files recursively and add to files.txt
for /r %%i in (*.py) do (
    echo %%i
    echo %%i >> files.txt
)
@echo ========================================================================

pause

:: Ask user if they want to create main .pot file
set /p CREATE_POT="Do you want to create new source English .pot file? (y/n): "

if /I "%CREATE_POT%"=="y" (
        :: Generate the base .pot file inside "locale"
        REM xgettext --from-code=UTF-8 --language=Python -o locale/messages.pot -f files.txt

        :: Run xgettext with debugging and generate the base .pot file inside "locale"
        REM xgettext --from-code=UTF-8 --keyword=gettext_gettext --output=locale/messages.pot --charset=UTF-8 --files-from=files.txt
        xgettext --from-code=UTF-8 --keyword=gettext_gettext --output=locale/messages.pot --files-from=files.txt

        :: Verify if .pot file was created
        if exist locale\messages.pot (
            echo Successfully created messages.pot!
        ) else (
            echo ERROR: Failed to generate messages.pot!
        )
)

pause

:: Ask user if they want to create .po files
set /p CREATE_PO="Do you want to create new language-specific .po files? (y/n): "
if /I "%CREATE_PO%"=="y" (
    for %%L in (%LANGUAGES%) do (
        if not exist locale\%%L\LC_MESSAGES mkdir locale\%%L\LC_MESSAGES
        if not exist locale\%%L\LC_MESSAGES\messages.po (
            copy locale\messages.pot locale\%%L\LC_MESSAGES\messages.po
            echo Created new: locale\%%L\LC_MESSAGES\messages.po
        ) else (
            echo Skipped: locale\%%L\LC_MESSAGES\messages.po already exists.
        )
    )
)

:: Ask user if they want to merge updated .pot content into existing .po files
set /p MERGE_PO="Do you want to merge updated .pot content into existing .po files? (y/n): "
if /I "%MERGE_PO%"=="y" (
    for %%L in (%LANGUAGES%) do (
        if exist locale\%%L\LC_MESSAGES\messages.po (
            msgmerge --update --backup=none locale\%%L\LC_MESSAGES\messages.po locale\messages.pot
            echo Merged updates into: locale\%%L\LC_MESSAGES\messages.po
        ) else (
            echo Skipping %%L: No messages.po found to merge.
        )
    )
)

:: Ask user if they want to compile .mo files
set /p CREATE_MO="Do you want to compile .mo files from .po files? (y/n): "
if /I "%CREATE_MO%"=="y" (
    for %%L in (%LANGUAGES%) do (
        if exist locale\%%L\LC_MESSAGES\messages.po (
            msgfmt -o locale\%%L\LC_MESSAGES\messages.mo locale\%%L\LC_MESSAGES\messages.po
            echo Compiled: locale\%%L\LC_MESSAGES\messages.mo
        ) else (
            echo Skipping %%L: No messages.po found.
        )
    )
)

:: Clean up files.txt
del files.txt

@echo ========================================================================
@echo Done: Localization setup is complete.
@echo ========================================================================
pause