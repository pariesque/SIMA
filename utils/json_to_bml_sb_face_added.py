import xml.etree.ElementTree as ET
from utils.dummy_parser import simple_parser
from engine.rules import gesture_mapping
from utils.dummy_parser import phrase_position

def create_speech_xml(characterName, parsed_text):
    """
    Utility function used to create speech xml string
    """
    #BML header
    #participant = ET.Element("participant")
    #participant.attrib["id"] = characterName
    #participant.attrib["role"] = "actor"

    t = parsed_text
    #bml = ET.Element("bml")
    if t is not None and len(t) > 0:
        speech = ET.Element("speech")
        speech.attrib["id"] = "sp1"
        speech.attrib["type"] = "application/ssml+xml"
        #if audioFile is not None:
            #speech.attrib["ref"] = str(audioFile)
    for i, (mark_name, word) in enumerate(parsed_text):
        start_mark = ET.Element("mark")
        start_mark.attrib["name"] = mark_name
        speech.append(start_mark)
        #word_text = ET.Element()
        start_mark.tail = word
        
        #speech.append(word_text)
        end_mark = ET.Element("mark")
        end_mark.attrib["name"] = f"T{i * 2 + 1}"
        speech.append(end_mark)
        speech_xml = ET.tostring(speech, encoding="unicode", method="xml")
    #bml.append(speech)
    #act = ET.Element("act")
    #act.append(participant)
    #act.append(bml)
    #return act, bml
    return speech_xml

def add_behavior_bml(speech_xml, behaviors, text):
    """
    Add behavior elements to the BML XML structure.
    """
    for behavior in behaviors:
        if not isinstance(behavior, dict):
            raise ValueError(f"Expected a dictionary, got {type(behavior)}: {behavior}")
        for behavior in behaviors: 
            behavior_elem = ET.Element("gesture")
            start_position = phrase_position(text, behavior["start"])
            behavior_elem.attrib["stroke_start"] = str("sp1:"+f'T{start_position}')
            #behavior_elem.attrib["relax"] = str("sp1:"+f'T{behavior["start"]}') ###
            if behavior["priority"] == "high":              ###
                behavior_elem.attrib["priority"] = "1"
            if behavior["priority"] == "medium":
                behavior_elem.attrib["priority"] = "2"
            if behavior["priority"] == "low":
                behavior_elem.attrib["priority"] = "3"
            else:
                behavior_elem.attrib["priority"] = "4" 
            behavior_elem.attrib["lexeme"] = gesture_mapping(str(behavior["type"]))
            if behavior["type"]=='Beat':
                behavior_elem.attrib["type"] = "BEAT"
            else:
                behavior_elem.attrib["type"] = "METAPHORIC"
            behavior_elem.attrib["emotion"] = "neutral"
            #behavior_elem.attrib["group"] = gesture_categorizer(str(behavior["type"]))     #lets skip this for now, we may add it later.
            speech_xml += ET.tostring(behavior_elem, encoding="unicode", method="xml")
            speech_xml += add_facial_expressions(behavior["type"], start_position)
    return speech_xml

def add_facial_expressions(lexeme, time):
    face_xml = ""
    #####################################
    if lexeme == "Collect":
        face_elem = ET.Element("head")
        face_elem.attrib["type"] = "TOSS"
        face_elem.attrib["amount"] = "-0.10"
        face_elem.attrib["repeats"] = "0.5"
        face_elem.attrib["start"] = str("sp1:"+f'T{time}')
        face_elem.attrib["end"] = str("sp1:"+f'T{time}+1.0')
        face_elem.attrib["group"] = "sweep"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")

        face_elem = ET.Element("head")
        face_elem.attrib["type"] = "nod"
        face_elem.attrib["amount"] = "0.15"
        face_elem.attrib["repeats"] = "0.5"
        face_elem.attrib["start"] = str("sp1:"+f'T{time}')
        face_elem.attrib["end"] = str("sp1:"+f'T{time}+0.5')
        face_elem.attrib["group"] = "sweep"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")

        face_elem = ET.Element("head")
        face_elem.attrib["type"] = "shake"
        face_elem.attrib["amount"] = "-0.25"
        face_elem.attrib["repeats"] = "0.5"
        face_elem.attrib["start"] = str("sp1:"+f'T{time}')
        face_elem.attrib["end"] = str("sp1:"+f'T{time}+1.0')
        face_elem.attrib["group"] = "sweep"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")
    #####################################
    if lexeme == "Container":
        face_elem = ET.Element("head")
        face_elem.attrib["id"] = "action2"
        face_elem.attrib["type"] = "shake"
        face_elem.attrib["amount"] = "-0.2"
        face_elem.attrib["repeats"] = "0.5"
        face_elem.attrib["start"] = str("sp1:"+f'T{time}')
        face_elem.attrib["relax"] = str("sp1:"+f'T{time}+0.8')
        face_elem.attrib["group"] = "shake_nod"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")

        face_elem = ET.Element("head")
        face_elem.attrib["type"] = "nod"
        face_elem.attrib["velocity"] = "1"
        face_elem.attrib["amount"] = "0.15"
        face_elem.attrib["repeats"] = "1"
        face_elem.attrib["start"] = "action2:start"
        face_elem.attrib["relax"] = "action2:relax+0.5"
        face_elem.attrib["group"] = "shake_nod"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")
    #####################################
    if lexeme == "Cycle":
        face_elem = ET.Element("face")
        face_elem.attrib["id"] = "blink"
        face_elem.attrib["type"] = "facs"
        face_elem.attrib["au"] = "45"
        face_elem.attrib["amount"] = "0.8"
        face_elem.attrib["start"] = str("sp1:"+f'T{time}')
        face_elem.attrib["end"] = str("sp1:"+f'T{time}+0.15')
        face_elem.attrib["side"] = "BOTH"
        face_elem.attrib["group"] = "small_nod"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")

        face_elem = ET.Element("head")
        face_elem.attrib["id"] = "action"
        face_elem.attrib["type"] = "nod"
        face_elem.attrib["velocity"] = "1"
        face_elem.attrib["amount"] = "0.07" ##previusly 0.05
        face_elem.attrib["repeats"] = "1"
        face_elem.attrib["start"] = "blink:start"
        face_elem.attrib["group"] = "small_nod"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")

        face_elem = ET.Element("head")
        face_elem.attrib["id"] = "overshoot"
        face_elem.attrib["type"] = "nod"
        face_elem.attrib["velocity"] = "1"
        face_elem.attrib["amount"] = "0.01"
        face_elem.attrib["repeats"] = "0.5"
        face_elem.attrib["start"] = "action:relax"
        face_elem.attrib["group"] = "small_nod"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")
    #####################################
    if lexeme == "Oscillation":
        face_elem = ET.Element("head")
        face_elem.attrib["type"] = "TOSS"
        face_elem.attrib["amount"] = "-0.25"
        face_elem.attrib["repeats"] = "0.5"
        face_elem.attrib["start"] = str("sp1:"+f'T{time}')
        face_elem.attrib["ready"] = str("sp1:"+f'T{time}+0.5')
        face_elem.attrib["relax"] = str("sp1:"+f'T{time}+0.7')
        face_elem.attrib["relax"] = str("sp1:"+f'T{time}+1.4')
        face_elem.attrib["group"] = "tilt_rt"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")

        face_elem = ET.Element("face")
        face_elem.attrib["type"] = "facs"
        face_elem.attrib["au"] = "2"
        face_elem.attrib["amount"] = "0.5"
        face_elem.attrib["relax"] = "$ready_time"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")

        face_elem = ET.Element("face")
        face_elem.attrib["type"] = "facs"
        face_elem.attrib["au"] = "1"
        face_elem.attrib["amount"] = "0.5"
        face_elem.attrib["relax"] = "$ready_time"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")
    #####################################
    if lexeme == "Negation":
        face_elem = ET.Element("head")
        face_elem.attrib["type"] = "shake"
        face_elem.attrib["amount"] = "0.2" #previously:0.03
        face_elem.attrib["repeats"] = "0.71"  #previously:1
        face_elem.attrib["start"] = str("sp1:"+f'T{time}')
        face_elem.attrib["group"] = "small_shake"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")
    #####################################
    if lexeme == "Offer":
        face_elem = ET.Element("head")
        face_elem.attrib["type"] = "nod"
        face_elem.attrib["velocity"] = "1"
        face_elem.attrib["amount"] = "-0.06"
        face_elem.attrib["repeats"] = "0.5"
        face_elem.attrib["sbm:smooth"] = "0.35"
        face_elem.attrib["start"] = str("sp1:"+f'T{time}')
        face_elem.attrib["group"] = "half_nod"
        face_xml += ET.tostring(face_elem, encoding="unicode", method="xml")

    return face_xml

def behaviors_to_bml(characterName, text, behaviors):
    # Create the base BML structure
    parsed_text = simple_parser(text)
    speech_xml = create_speech_xml(characterName, parsed_text)
    # Add behaviors
    xml_str = add_behavior_bml(speech_xml, behaviors, text)
    # Convert the entire XML tree to a string
    #xml_str = ET.tostring(speech_xml, encoding="unicode", method="xml")
    #with open(f"{text}.xml", "w") as output_file:
    with open("xml_file.xml", "w") as output_file:
        output_file.write(xml_str)
    return xml_str

