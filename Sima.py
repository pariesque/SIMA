import os
#import logging
#import logging.config
import json
from datetime import datetime

from utils import json_to_bml_sb_face_added
#import engine #fix this
from engine import agent
#from config import params #fix this

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from xml.dom import minidom

# Import Pyke, import engines . all engines are all globals
#from pyke import knowledge_engine
#from engine import rules 

#from engine.data import InitSemantics as sem
#nvbg_engine = knowledge_engine.engine(rules)  #probably we would not want this, beacuse it uses rules

# from listen import listen_dcaps as listen

# Load data
#from engine.data import UniversalFactUtil
#dataPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "engine", "data")
#print("dataPath: ", dataPath)

#exec(open(os.path.join(dataPath, 'InitSemantics.py')).read())
#exec(open(os.path.join(dataPath, 'InitNVBGGlobalSetting.py')).read())
#exec(open(os.path.join(dataPath, 'InitBrainStemGlobalSetting.py')).read())
#exec(open(os.path.join(dataPath, 'InitDefaultBehaviorBMLMapping.py')).read())

# dataPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "engine\\data\\")
# execfile(dataPath + 'InitSemantics.py')
# execfile(dataPath + 'InitNVBGGlobalSetting.py')
# execfile(dataPath + 'InitBrainStemGlobalSetting.py')
# execfile(dataPath + 'InitDefaultBehaviorBMLMapping.py')

# Load the project specific data
#dataPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), params.PROJECT_SPECIFIC_PATH)
#exec(open(dataPath + 'InitCharacterBehaviorBMLMapping.py').read())
#exec(open(dataPath + 'InitPersonalityBehaviorBMLMapping.py').read())

# setup the logger
now = datetime.now().strftime("%y%m%d_%H%M%S")
#logging.config.fileConfig('config/log.conf', defaults={'logfilename': './tmp/' + now + '.log'})
#logger = logging.getLogger("Sima")


class SIMA:
    """ main class """

    def __init__(self, characterName):
        """ Initialization """
        self.characterName = ""
        self.pushToTalk = False
        self.speechWindowLow = 8000
        self.speechWindowUp = 12000
        self.behTimeMap = {}
        self.prevBehList = []
        self.curEmotion = "neutral"
        self.curPosture = ""
        self.curPersonality = "extravert"
        self.isSpeaking = None
        self.stop = False
        self.new_beh_count = 0
        #sem.loadSemanticsFacts(self.getEngine())
        #logger.info("Initialization done.")

    def createEngine(self): 
        global inference_engine 
        inference_engine = agent.gesture_agent(model = "gpt-4")
        return 
    
    def getEngine(self):
        return  inference_engine


    def generate(self, characterName, txt, analysis=True, generation=False):
                
        self.createEngine()
        if analysis:
            return self.analysis(characterName, txt)
        if generation:
            return self.BML_generation(characterName, txt)
        #logger.info("generation done.")


    def analysis(self, characterName, txt): 
        self.new_beh_count = 0
        new_behs = inference_engine.run(txt)
        new_behs_list = new_behs.split(",\n")
        if new_behs_list is not None and len(new_behs_list)!=0:
            for beh in new_behs_list:
                beh = json.loads(beh)
                self.prevBehList.append(beh) #check the json here
                self.new_beh_count +=1
            return self.prevBehList[-self.new_beh_count:] #return the new generated behaviors


    def BML_generation(self, characterName, txt, offset=0): ###this function is not used for now
        """
        Generate the BML, returns it as a string.
        opt. writes the BML in the file 'outputfilename'
        opt. writes the log in the file 'logfilename'
        """
        #logger.debug("start bml generation.")
        #self.load_behaviors() ####fix this
        #nvbg_engine.assert_('nvbg', 'char', ('name', characterName))

        # Insert emotion status
        """
        if self.curEmotion != 'neutral':
            nvbg_engine.assert_('nvbg', 'emotion', (characterName, self.curEmotion, ''))
        # Insert personality status
        nvbg_engine.assert_('nvbg', 'personality', (characterName, self.curPersonality, ''))
        # Run the Engine
        self.getEngine().activate('bml_generate')
        logger.info("bml generation done.")
        # self.getEngine().get_kb('nvbg').dump_universal_facts()
        # Write the logFile if requested
        if logfilename:
            logger.debug("write logFile %s.", logfilename)
            # content = self.getEngine().get_kb('nvbg').retrieve_specific_facts()
            content = self.retrieve_all_specific_facts('nvbg')
            with open(logfilename, 'w') as f:
                f.write(content)
        # Save the generated behaviors
        self.save_behaviors()
        """

        # Generate the BML structure
        #logger.debug("start generating BML XML.")
        # Generate the BML tree
        # note: should optimize that, write to a string then parse it to
        # extract what was converted is not optimal
        #xml_output = json_to_bml(self.prevBehList[-1])             #######use this later
        #out = inference_engine.run(txt)
        #print(out)
        """
        json_checker_bool = self.json_checker(out)
        if json_checker_bool == True:
            self.prevBehList.append(out)
        else:
            print("the json file was invalid")
            out = inference_engine.run(txt)
        """
        new_behaviors = self.prevBehList[-self.new_beh_count:]

    def json_checker(self, json_string):
        try:
            data = json.loads(json_string)
            return True
        except json.JSONDecodeError:
            return False