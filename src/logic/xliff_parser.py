from lxml import etree

def parse_xliff(file_path):
    tree = etree.parse(file_path)
    segments = []

    for trans_unit in tree.xpath("//trans-unit"):
        seg_id = trans_unit.get("id")
        source = trans_unit.findtext("source", "")
        target = trans_unit.findtext("target", "")
        segments.append((seg_id, source, target))

    return segments
