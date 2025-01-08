import os
import openai
from openai import OpenAI
import json
import time



class gesture_agent ():
  OPENAI_API_KEY = "YOUR_API_KEY"
  client = OpenAI(api_key=OPENAI_API_KEY)
  
  def __init__(self, model):
    self.model = model
    self.prompt_init = ""

    self.prompt = f""" Here is a list of Gesture types, their description, and some examples:
        - Cycle: This gesture represents actions or processes that repeat in a continuous loop or follow a recurring pattern.
            Example: The speaker says "I think you have to look at obviously industry by industry.". She uses a Cycle Gesture to illustrate the phrase "look at obviously industry by industry".
        - Collect: This gesture represents gathering, collecting, or bringing things together, into one entity. 
            Example: The speaker says "So, I think just putting out a plug for the idea of coming together collectively, right? And exercising your voice to give you more strength and protection is what unions are all about.". She uses a Collect Gesture to illustrate the phrase "coming together collectively, right? And exercising your voice".
        - Container: This gesture represents a boundary, a sweep, or an imaginary box holding a collection of items.
            Example: The speaker says "It's kind of risky sometimes asking for these things ,and if you don't have the protection of a collective bargaining agreement or a union ". She uses a Container Gesture to illustrate the phrase "collective bargaining".
            Example: The speaker says "It's kind of risky sometimes asking for these things ,and if you don't have the protection of a collective bargaining agreement or a union ". She uses a Container Gesture to illustrate the phrase "union".
            Example: The speaker says "I mean, the notion of asking for what you need, often you are -- there's a lot of risk there.". She uses a Container Gesture to illustrate the phrase "a lot of risk".
        - Oscillation: This gesture represents alternation, uncertainty, or indecision, or items being out of balance. 
            Example: The speaker says "So, sometimes scheduling might not be necessarily as much of an issue for some of these work-family types of concepts than other issues, such as paid leave, paid sick leave, paid family leave.". She uses a Oscillation Gesture to illustrate the phrase "work-family types of concepts".
        - Negation: This gesture represents disagreement, refusal, or denial.
        - Offer: This gesture represents invitation, presentation, and a willingness to share or request acceptance.
        - Beat: This gesture is a rythmic hand movement used to emphasize words or phraseS in the speech, without carrying semantic meanings.
    I will provide you with a speech from a speaker.
    For each utterance in the speech, Please identify all the possible co-speech gestures.
    Only report in the following json formats, no other text.
            Here is an example:
                {json.dumps({
                    "type": "the gesture type",
                    "start": "the word where the gesture happens",
                    "priority": "the priority of the gesture: high, medium, or low"
                })}
            """
    
    self.prompt_init = self.prompt
   

  def run_assistant(self, message, model, temperature, max_tokens, frequency_penalty):
        response =  self.client.chat.completions.create(
            model= self.model,
            messages = message,
            temperature= temperature,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty
        )
        output = response.choices[0].message.content
        return output

  def run(self, utter):
        prompt = self.prompt_init + "\n" + "The speaker says: " +f' "{utter}" '
        message = [{"role": "user", "content": prompt}]
        output = self.run_assistant(message,"gpt-4",0.2,256,0.)
        return output




