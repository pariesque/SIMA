#import logging

from Sima import SIMA as SIMAObj
import os
import json
from utils.json_to_bml_sb_face_added import behaviors_to_bml
# Create the logger
#logger = logging.getLogger("Cerebellm.main")
characterName = 'Olivia'
sima = SIMAObj(characterName)

if __name__ == '__main__':
    while True:
        text = input("\n Enter your text:   ")
        characterName = "ChrOlivia"
        out = sima.generate(characterName, text, analysis=True, generation=False)
        print(out)
        xml_output = behaviors_to_bml(characterName, text, out)
        #print(xml_output)
        command = f"bml.execBML('{characterName}', '{xml_output}')"
        with open('exec.py', 'w') as file:
            file.write(command)
        
