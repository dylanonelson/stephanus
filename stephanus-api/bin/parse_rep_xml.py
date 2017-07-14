import json
import xml.etree.ElementTree as ET

tree = ET.parse('./static/tlg0059.tlg030.perseus-grc1.xml')

root = tree.getroot()

# Just Book One for now
root = root.find('.//div[@type=\'book\'][@n=\'1\']')

result = {}

for section in root.findall('div[@type=\'section\']'):
    textNodes = []

    for said in section.iter('said'):
        paragraph = { 'text': said.text }
        textNodes.append(paragraph)

        for child in said.findall('milestone[@unit=\'para\']'):
            paragraph = { 'text': child.tail }
            textNodes.append(paragraph)

    result[section.attrib['n']] = textNodes

print (result)
