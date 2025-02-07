import re
import gettext

# Initialize gettext for translations
_ = gettext.gettext

def check_segments(segments):
    results = []

    for seg_id, source, target in segments:
        if not target:
            status = _("ERROR: ❌ Untranslated Segment")
        elif not validate_tags(source, target):
            status = _("ERROR: ⚠️ Mismatched Tags")
        else:
            status = _("✅ Correct")

        results.append((seg_id, source, target, status))

    return results

def validate_tags(source, target):
    """Checks if tags in the source match the target."""
    source_tags = set(re.findall(r"<.*?>", source))
    target_tags = set(re.findall(r"<.*?>", target))
    return source_tags == target_tags
