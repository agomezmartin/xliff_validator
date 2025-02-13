import gettext

# ✅ Set the language for the application
LANGUAGE = "es"  # Change to "en" for English, "fr" for French, etc.

translation = gettext.translation("messages", localedir="locale", languages=[LANGUAGE], fallback=True)
gettext_gettext = translation.gettext  # ✅ Export this variable
