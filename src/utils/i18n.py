import gettext

# ✅ Set the language for the application
LANGUAGE = "en"  # Change between "en" for English, "es" for Spanish or "fr" for French.

translation = gettext.translation("messages", localedir="locale", languages=[LANGUAGE], fallback=True)
gettext_gettext = translation.gettext  # ✅ Export this variable
