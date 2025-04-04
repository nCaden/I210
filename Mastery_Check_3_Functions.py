def calculate_lenth(text): #takes the text and uses the len function to return the length of the string
    return len(text)

def count_vowels(text): #using an if statement inside a for loop, the funciton will itirate through the text and count all of the vowels we have defined in the vowels list
    vowels = ["a", "e", "i", "o", "u", "y"] #sometimes y so I included y
    count = 0
    for char in text.lower(): #ensures function even if the vowel is a capital letter
        if char in vowels:
            count+=1
    return count

def count_words(text): #takes text and splits where there are spaces that seperate individual words and then uses the len function to count them
    return len(text.split())

def count_sentances(text): #uses a for loop and if statement to iterate through the input and count how many sentances there are from seeing how many punctuation marks there are
    punctuation = [".", "!", "?"]
    count = 0
    for char in text:
        if char in punctuation:
            count+=1
    return count

def puncuation_remover(text): #iterates through the text and finds instances of punctuation marks and removes them using the replace function, the text varaible is then updated and returned
    punctuation = [".", "!", "?"]
    for char in text:
        if char in punctuation:
            text = text.replace(char, "")
    return text

def letter_frequency(text): #iterates through the text and adds every character present and counts how many times that character appears by using +=1 and =1
    text = text.lower() #makes all text lowercase to get around case sensitivity
    frequency = {} #intializes empty dictionary
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency