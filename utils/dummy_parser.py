import string

def simple_parser(sentence):
    words = sentence.split()
    parsed = []
    
    for i, word in enumerate(words):
        mark = f"T{i*2}"
        parsed.append((mark, word))
    
    return parsed

#this creates the parsed part of the bml file


def phrase_position(sentence, phrase):
    # Convert both to lowercase and remove punctuation for case-insensitive search
    sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation))
    phrase = phrase.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Initialize an empty list to store the starting positions of the phrase
    positions = []
    phrase_length = len(phrase.split())
    
    # Split the sentence into words
    words = sentence.split()
    
    # Loop through the words with a window size equal to the phrase length
    for i in range(len(words) - phrase_length + 1):
        # Check if the current window matches the phrase
        if ' '.join(words[i:i + phrase_length]) == phrase:
            positions.append(i*2)
    
    return int(positions[0])
