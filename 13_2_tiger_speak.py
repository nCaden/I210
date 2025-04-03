# 13.2 Tiger speak

# Remember, imports go at the top!
import random

# Write a function "tiger_speak": (takes a string, returns a string)
# Rules for tiger speak:
# ----Each character is **randomly** upper or lower case
# ----Every space is now a dash - tigers have stripes!
def tiger_speak(sentence):
    new_sentance = ""
    for letter in sentence:
        random.randint(0, 1)
        if letter == 0:
            new_sentance += letter.upper()
        elif letter == 1:
            new_sentance += letter.lower()
    return new_sentance.replace(" ","-")

  
# main

# Get a sentence from the user, pass it through the function
# print the result.
message = input("Enter a message: ")
my_tiger = tiger_speak(message)
print(my_tiger)
