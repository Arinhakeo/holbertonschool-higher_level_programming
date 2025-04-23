#!/usr/bin/python3


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result_dict = {child.tag: child.text for child in root}
        return result_dict

    except Exception as e:
        print(f"Erreur lors de la désérialisation : {e}")
        return None

if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionnaire sérialisé dans {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDonnées désérialisées :")
    print(deserialized_data)
