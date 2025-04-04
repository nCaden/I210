from Mastery_Check_3_Functions import*

####################################################
text = input("Enter in some text: ") #grabs user input

#assigning the variables to functions

length = calculate_lenth(text)
num_vowels = count_vowels(text)
num_words = count_words(text)
num_sentances = count_sentances(text)
no_punctuation = puncuation_remover(text)
frequency = letter_frequency(text)

#function calls
print(f"The length of the entered text is: {length}")
print(f"That text contains {num_vowels} vowels")
print(f"Words contained in that text: {num_words}")
print(f"Number of sentances: {num_sentances}")
print(f"Without punctuation that would like: {no_punctuation}")
print(f"Letters present and frequency: {frequency}")
