import gettext

def setup_translations():
    """Sets up internationalization using gettext."""
    gettext.bindtextdomain("messages", "SRC/translations")
    gettext.textdomain("messages")
    return gettext.gettext
