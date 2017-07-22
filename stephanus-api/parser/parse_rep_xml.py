import json
import os
import xml.etree.ElementTree as ET

def parse_book_one():
    dir = os.path.dirname(__file__)
    fn = os.path.join(dir, '../static/tlg0059.tlg030.perseus-grc1.xml')

    tree = ET.parse(fn)

    root = tree.getroot()

    # Just Book One for now
    root = root.find('.//div[@type=\'book\'][@n=\'1\']')

    result = []

    # Each section represents a Stephanus page + letter
    for section in root.findall('div[@type=\'section\']'):
        page_content = []
        page = { 'id': section.attrib['n'], 'content': page_content }

        # In the book one xml, each section containes one nested <said>
        for said in section.iter('said'):
            said_who = said.attrib['who']
            continued_text = []
            continued_paragraph = {'type': 'paragraph',
                                   'continued': True,
                                   'content': continued_text,
                                   'speaker': { 'name': said_who}}
            continued_text.append({'type': 'text', 'text': said.text})
            page_content.append(continued_paragraph)

            for child in said.findall('milestone[@unit=\'para\']'):
                text_nodes = []
                text_nodes.append({'type': 'text', 'text': child.tail})
                paragraph = {'type': 'paragraph',
                             'continued': False,
                             'speaker': {'name': said_who},
                             'content': text_nodes}

                page_content.append(paragraph)

        result.append(page)

    return result

if __name__ == '__main__':
    pretty_json = json.dumps(parse_book_one(), indent=4, ensure_ascii=False)
    print (pretty_json)
