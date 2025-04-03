# 13.1 Shout and whisper

# FUNCTION: "shout" that takes a string and modifies it as follows:
# Sentences that end in . or no punctuation should end in !!!
# Sentences that end in ! should also end in !!!
# Sentences that end in ? should end in ???
# CAPITALIZE ALL LETTERS!
def shout(sentence):
    """converts a sentence into all uppercase with triple end punctuation"""
    sentence = (sentence.strip().upper())

    if sentence[-1] == "!":
        sentence 


# FUNCTION: "whisper" that takes a string and modifies it as follows:
# Sentences that end in ??? should end in ?
# Sentences that end in !!! should end in .
# lowercase all of the letters
def whisper(sentence):
    """converts a sentence into all lowercase with single punctuation"""   
    sentence = (message.lower())

    if sentence[-3:] == "???":
        sentence = sentence[:-3] + "?"
    
    return sentence

# main

# INPUT: get a message from the user
message = input("Enter a sentence: ")

# PROCESSING & OUTPUT: convert the message to a shout and print the result
# Call the function and save what it returns!
my_shout = shout
print(my_shout(message))
# PROCESSING & OUTPUT: convert the shout to something quiet and print the result
# Call the function and save what it returns!
my_whisper = whisper
print(my_whisper(message))

