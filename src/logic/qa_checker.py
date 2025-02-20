import xml.etree.ElementTree as ET
import re
from src.utils.logs_config import logging
from src.utils.i18n import gettext_gettext  # ✅ Import translation

# ✅ Define XLIFF namespace (avoids repeated dictionary creation)
ns = {"xliff": "urn:oasis:names:tc:xliff:document:1.2"}  # XLIFF 1.2 namespace

def parse_xliff(file_path):
    """ ✅ Extracts XLIFF segments for QA validation. """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        segments = []

        for trans_unit in root.findall(".//xliff:trans-unit", ns):
            segment_id = trans_unit.get("id", "N/A")
            source_text = trans_unit.find("xliff:source", ns).text or ""
            target_elem = trans_unit.find("xliff:target", ns)
            target_text = target_elem.text if target_elem is not None else ""

            qa_status = check_segment(source_text, target_text)

            segments.append((segment_id, source_text, target_text, qa_status))

        logging.info(gettext_gettext("Segments extracted and validated successfully."))

        return segments

    except ET.ParseError:
        logging.error(gettext_gettext("Error: The XLIFF file is corrupted or unreadable."))
        return gettext_gettext("Error: The XLIFF file is corrupted or unreadable.")

    except Exception as e:
        logging.error(gettext_gettext("Error: ") + str(e))
        return gettext_gettext("Error: ") + str(e)

def check_segment(source, target):
    try:
        """ ✅ QA validation rules. """
        if not target.strip():
            return gettext_gettext("Untranslated segment")
    
        if not source.strip():
            return gettext_gettext("Source missing")

        if target==source:
            return gettext_gettext("Source in target")

        if has_mismatched_tags(source, target):
            return gettext_gettext("Mismatch/missing tag")
    
        if is_pseudotranslated(target):
            return gettext_gettext("Pseudotranslated")

        return gettext_gettext("Correct")
    
    except Exception as e:
        logging.error(gettext_gettext(f"Error on QA validation rules: {e}"))
        return gettext_gettext(f"Error on QA validation rules: {e}")

def has_mismatched_tags(source, target):
    """Checks if tags are mismatched, missing, out of order, or incorrectly nested."""    
    def extract_tags(segment):
        try:
            """Extracts tags and checks for proper nesting using a stack."""
            tags = re.findall(r'</?[^>]+>', segment)  # Extract all tags using regular expressions
            stack = []  # Stack to check nesting
        
            for tag in tags:
                if not tag.startswith("</"):  # Opening tag
                    stack.append(tag)
                else:  # Closing tag
                    if not stack:
                        return False  # Unmatched closing tag
                
                    last_tag = stack.pop()
                    if last_tag[1:] != tag[2:]:  # Compare <tag> with </tag>
                        return False  # Mismatched tag
        
            return not stack  # ✅ If stack is empty, nesting is correct

        except Exception as e:
            logging.error(gettext_gettext(f"Error extracting segment tags: {e}"))
            return gettext_gettext(f"Error extracting segment tags: {e}")
    
    try:

        logging.info(gettext_gettext("Mismatched tags checked correctly."))
        return extract_tags(source) != extract_tags(target) # ✅ Tags in both source and target segments are checked. Returns TRUE if mismatches are found.
    
    except Exception as e:
        logging.error(gettext_gettext(f"Error checking mistmatched tags: {e}"))
        return gettext_gettext(f"Error checking mistmatched tags: {e}")

def is_pseudotranslated(target):
    try:
        """ ✅ Checks if target text follows pseudotranslation patterns. """
        return (target.startswith("#") and target.endswith("$")) or (target.startswith("_") and target.endswith("_"))
    
    except Exception as e:
        logging.error(gettext_gettext(f"Error checking pseudotranslated segments: {e}"))
        return gettext_gettext(f"Error checking pseudotranslated segments: {e}")
