from PySide6.QtGui import QColor, QTextCharFormat, QTextCursor
from PySide6.QtWidgets import QTextEdit
import xml.etree.ElementTree as ET
import re
from src.utils.logs_config import logging
from src.utils.i18n import gettext_gettext  # ✅ Import translation

def extract_text_with_tags(element):
    """ ✅ Extracts both text and inline tags while highlighting internal tags. """
    if element is None:
        return [], ""

    formatted_result = []  # ✅ For GUI display (formatted text)
    plain_text_result = ""  # ✅ For QA check (plain text)

    blue_format = QTextCharFormat()
    blue_format.setForeground(QColor("blue"))  # ✅ Set blue color for internal tags

    for node in element.iter():
        if node.tag == element.tag:  # Skip root node itself
            if node.text:
                formatted_result.append((node.text, QTextCharFormat()))  # Normal text
                plain_text_result += node.text  # Add plain text
            continue

        tag_str = ET.tostring(node, encoding="unicode", method="xml")

        # ✅ REMOVE namespace (e.g., "ns0:")
        tag_str = re.sub(r'\s+xmlns(:\w+)?="[^"]+"', '', tag_str)
        tag_str = re.sub(r'\w+:', '', tag_str)  # Remove any remaining namespace prefixes
        tag_str = re.sub(r'"(\s?)(/?)>', r'"\2>', tag_str)  # Fix malformed self-closing tags

        # ✅ Build segment with format (for GUI) and without format (for QA)
        if node.text:
            formatted_result.append((node.text, QTextCharFormat()))  # Normal text
            plain_text_result += node.text  # Add plain text

        formatted_result.append((tag_str, blue_format))  # ✅ Internal tag in blue
        plain_text_result += tag_str  # ✅ Keep tags in plain text for QA

#        if node.tail:
#            formatted_result.append((node.tail, QTextCharFormat()))  # Normal text after tag
#            plain_text_result += node.tail  # Add to plain text

    return formatted_result, plain_text_result  # ✅ Returns formatted (for GUI) & plain text (for QA)

def check_segment(source_plain, target_plain):
    """ ✅ QA validation rules. """
    try:
        if not target_plain.strip():
            return gettext_gettext("Untranslated segment")

        if not source_plain.strip():
            return gettext_gettext("Source missing")

        if target_plain == source_plain:
            return gettext_gettext("Source in target")

        if has_mismatched_tags(source_plain, target_plain):
            return gettext_gettext("Mismatch/missing tag")

        if has_mismatched_numbers(source_plain, target_plain):
            return gettext_gettext("Mismatch/missing number")

        if is_pseudotranslated(target_plain):
            return gettext_gettext("Pseudotranslated")

        return gettext_gettext("Correct")

    except Exception as e:
        logging.error(gettext_gettext(f"Error on QA validation rules: {e}"))
        return gettext_gettext(f"Error on QA validation rules: {e}")

def has_mismatched_tags(source_plain, target_plain):
    """ ✅ Checks if internal tags are mismatched, missing, or out of order. """
    def extract_tags(segment):
        """ ✅ Extracts **all** tags (standard + self-closing) while preserving order. """
        return re.findall(r'</?[^>]+?>', segment)  # ✅ Extracts **all** tags (opening, closing, self-closing)

    try:
        return extract_tags(source_plain) != extract_tags(target_plain)  # ✅ Returns True if mismatches are found

    except Exception as e:
        logging.error(gettext_gettext(f"Error checking mismatched tags: {e}"))
        return gettext_gettext(f"Error checking mismatched tags: {e}")

def has_mismatched_numbers(source_plain, target_plain):
    """ ✅ Checks if internal numbers are mismatched, missing, or out of order. """
    def extract_numbers(segment):
        """ ✅ Extracts **all** numbers while preserving order. """
        # return re.findall(r'</?[^>]+?>', segment)  # ✅ Extracts **all** tags (opening, closing, self-closing)
        return re.findall(r'-?\d+(?:[.,]\d+)?', segment)  # ✅ Extracts **all** numbers

    try:
        return extract_numbers(source_plain) != extract_numbers(target_plain)  # ✅ Returns True if mismatches are found

    except Exception as e:
        logging.error(gettext_gettext(f"Error checking mismatched numbers: {e}"))
        return gettext_gettext(f"Error checking mismatched numbers: {e}")

def is_pseudotranslated(target_plain):
    """ ✅ Checks if the target follows pseudotranslation patterns. """
    try:
        return (target_plain.startswith("#") and target_plain.endswith("$")) or (target_plain.startswith("_") and target_plain.endswith("_"))

    except Exception as e:
        logging.error(gettext_gettext(f"Error checking pseudotranslated segments: {e}"))
        return gettext_gettext(f"Error checking pseudotranslated segments: {e}")

def display_colored_text(text_segments, text_edit_widget):
    """ ✅ Inserts extracted segments with internal tags in blue inside a QTextEdit widget. """
    text_edit_widget.clear()
    cursor = text_edit_widget.textCursor()

    for text, format in text_segments:
        cursor.insertText(text, format)  # ✅ Insert text with correct format
