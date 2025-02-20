from lxml import etree
from src.utils.logs_config import logging
from src.utils.i18n import gettext_gettext  # ✅ Import translation

def parse_xliff(file_path):
    try:
        tree = etree.parse(file_path)
        segments = []

        for trans_unit in tree.xpath("//trans-unit"):
            seg_id = trans_unit.get("id")
            source = trans_unit.findtext("source", "")
            target = trans_unit.findtext("target", "")
            segments.append((seg_id, source, target))
    
        logging.info(gettext_gettext("Segments extracted successfully.")

        return segments
    except Exception e:
        logging.error(gettext_gettext(f"Error extracting segments: {e}"))
        return gettext_gettext(f"Error extracting segments: {e}")
