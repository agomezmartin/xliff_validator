import gettext
from src.utils.compiler import localedir # ✅ Import locale or _internal/locale variable

# ✅ Set the language for the application
LANGUAGE = "fr"  # Change to "en" for English, "es" for Spanish or "fr" for French.

# ✅ Initialize gettext
translation = gettext.translation("messages", localedir=localedir, languages=[LANGUAGE], fallback=True)
gettext_gettext = translation.gettext  # ✅ Export this variable
