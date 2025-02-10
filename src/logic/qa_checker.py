import xml.etree.ElementTree as ET
import re
import gettext

gettext.bindtextdomain("messages", "locale")
gettext.textdomain("messages")
translation = gettext.translation("messages", "locale", fallback=True)
gettext_gettext = translation.gettext

def parse_xliff(file_path):
    """ ✅ Extracts XLIFF segments for QA validation. """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # ✅ Handle XLIFF versions
        ns = {"xliff": "urn:oasis:names:tc:xliff:document:1.2"}  # XLIFF 1.2 namespace
        segments = []

        for trans_unit in root.findall(".//xliff:trans-unit", ns):
            segment_id = trans_unit.get("id", "N/A")
            source_text = trans_unit.find("xliff:source", ns).text or ""
            target_elem = trans_unit.find("xliff:target", ns)
            target_text = target_elem.text if target_elem is not None else ""

            qa_status = check_segment(source_text, target_text)

            segments.append((segment_id, source_text, target_text, qa_status))

        return segments

    except ET.ParseError:
        return gettext_gettext("Error: The XLIFF file is corrupted or unreadable.")
    except Exception as e:
        return gettext_gettext("Error: ") + str(e)

def check_segment(source, target):
    """ ✅ QA validation rules. """
    if not target.strip():
        return gettext_gettext("Untranslated segment")
    
    if not source.strip():
        return gettext_gettext("Source missing")
    
    if has_mismatched_tags(source, target):
        return gettext_gettext("Mismatch/missing tag")
    
    if target.startswith("#") and target.endswith("$"):
        return gettext_gettext("Pseudotranslated")

    if target.startswith("_") and target.endswith("_"):
        return gettext_gettext("Pseudotranslated")

    return gettext_gettext("Correct")

def has_mismatched_tags(source, target):
    """ ✅ Checks if tags are mismatched/missing or out of order. """
    # Use regular expression to extract tags and text content
    source_tags = re.findall(r'<[^>]+>', source)
    target_tags = re.findall(r'<[^>]+>', target)

    # Check if the tags are the same in order and position
    return source_tags != target_tags