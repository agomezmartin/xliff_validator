import gettext

# ✅ Set the language for the application
LANGUAGE = "es"  # Change between "en" for English or "es" for Spanish.

translation = gettext.translation("messages", localedir="locale", languages=[LANGUAGE], fallback=True)
gettext_gettext = translation.gettext  # ✅ Export this variable
