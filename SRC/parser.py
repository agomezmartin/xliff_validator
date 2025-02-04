import xml.etree.ElementTree as ET
import gettext

# Initialize gettext for translations
gettext.bindtextdomain("messages", "SRC/translations")
gettext.textdomain("messages")
_ = gettext.gettext  # Shortcut for translations

def parse_xliff(file_path):
    """Parse the XLIFF file and validate its segments.

    Args:
        file_path (str): The path to the XLIFF file.

    Returns:
        List of tuples containing:
            (segment_id, source_text, target_text, error_message)
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Tupple to save QA results
    segments = []

    # Translation units are extracted
    for trans_unit in root.findall(".//trans-unit"):
        seg_id = trans_unit.get("id", "N/A")  # Extract segment ID
        source = trans_unit.find("source").text or ""  # Extract source text
        target = trans_unit.find("target").text or ""  # Extract target text

        # QA Checks: source and targets are QAed
        error = None
        if not target:
            error = gettext.gettext("Missing Translation")  # Error if target is empty
        elif "<" in source and ">" in source and "<" in target and ">" not in target:
            error = gettext.gettext("Tag Mismatch")  # Error if source has tags but target doesn't

        segments.append((seg_id, source, target, error))  # Append to list

    return segments  # Return parsed data
