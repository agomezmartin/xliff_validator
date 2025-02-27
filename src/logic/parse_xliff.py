import xml.etree.ElementTree as ET
import re
from PySide6.QtGui import QColor, QTextCharFormat
from src.utils.logs_config import logging
from src.utils.i18n import gettext_gettext  # ✅ Import translation
from src.logic.qa_checker import extract_text_with_tags, check_segment, display_colored_text

# ✅ Define XLIFF namespace
ns = {"xliff": "urn:oasis:names:tc:xliff:document:1.2"}  # XLIFF 1.2 namespace

def parse_xliff(file_path, text_edit_widget_source, text_edit_widget_target):
    """ ✅ Extracts XLIFF segments while preserving internal tags & displays them in QTextEdit widgets. """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        segments = []

        for trans_unit in root.findall(".//xliff:trans-unit", ns):
            segment_id = trans_unit.get("id", "N/A")

            source_elem = trans_unit.find("xliff:source", ns)
            target_elem = trans_unit.find("xliff:target", ns)

            # ✅ Extract **formatted** text (for GUI) and **plain** text (for QA check)
            source_text, source_plain = extract_text_with_tags(source_elem)
            target_text, target_plain = extract_text_with_tags(target_elem) if target_elem is not None else ("", "")

            # ✅ Perform QA on segments
            qa_status = check_segment(source_plain, target_plain)

            # ✅ Display colored text in QTextEdit widgets
            display_colored_text(source_text, text_edit_widget_source)
            display_colored_text(target_text, text_edit_widget_target)

            segments.append((segment_id, source_plain, target_plain, qa_status))

        logging.info(gettext_gettext("Segments extracted successfully."))

        return segments

    except ET.ParseError:
        logging.error(gettext_gettext("Error: The XLIFF file is corrupted or unreadable."))
        return gettext_gettext("Error: The XLIFF file is corrupted or unreadable.")

    except Exception as e:
        logging.error(gettext_gettext("Error: ") + str(e))
        return gettext_gettext("Error: ") + str(e)
