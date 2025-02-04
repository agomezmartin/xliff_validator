import xml.etree.ElementTree as ET
import gettext

_ = gettext.gettext  # Translation shortcut

def parse_xliff(file_path):
    """Parse the XLIFF file and validate its segments."""
    tree = ET.parse(file_path)
    root = tree.getroot()

    segments = []
    for trans_unit in root.findall(".//trans-unit"):
        seg_id = trans_unit.get("id", "N/A")
        source = trans_unit.find("source").text or ""
        target = trans_unit.find("target").text or ""

        error = None
        if not target:
            error = _("Missing Translation")
        elif "<" in source and ">" in source and "<" in target and ">" not in target:
            error = _("Tag Mismatch")

        segments.append((seg_id, source, target, error))

    return segments
