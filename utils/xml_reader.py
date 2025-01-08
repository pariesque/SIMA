import xml.etree.ElementTree as ET

def read_xml_file(file_path):
    # Load and parse the XML file
    tree = ET.parse(file_path)
    
    # Get the root element
    root = tree.getroot()
    
    # Print the root element tag
    print("Root Tag:", root.tag)
    
    # Iterate through the elements and print their tag and attributes
    for elem in root.iter():
        print(f"Tag: {elem.tag}, Attributes: {elem.attrib}, Text: {elem.text.strip() if elem.text else ''}")

    # Example: Find a specific element by tag
    speech_elem = root.find('bml/speech')
    if speech_elem is not None:
        print("Speech Text:", speech_elem.text)
    
    # Example: Find all gesture elements
    gestures = root.findall('.//gesture')
    for gesture in gestures:
        print("Gesture:", gesture.attrib)

if __name__ == "__main__":
    file_path = '/Users/ghanadtorshizi.p/Virtual Human/output.xml' 
    read_xml_file(file_path)
