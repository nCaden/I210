#Sentence Manager
import random

#method for random case
def randomcase(sentence):
    new_case = ""
    for letter in sentence:
        case =random.randint(0, 1)
        if case == 0:
            new_case += letter.upper()
        elif case == 1:
            new_case += letter.lower()
    return new_case
my_randomcase = randomcase
print("Welcome to the Sentence Manager")

sentence = input("Enter a sentence: ")
#Main
while True:

    print("How would you like to change your sentence?")

    print("Option #1 - Change sentence to uppercase")
    print("Option #2 - Change sentence to lowercase")
    print("Option #3 - Change sentence to random case")
    print("Option #4 - Replace part of sentence")

    option = int(input())

    if option == 1:
        sentence = sentence.upper()
 

    elif option == 2:
        sentence = sentence.lower()
        

    elif option == 3:
        sentence = (my_randomcase(sentence))
        

    elif option == 4:
        #replacement
        old_string = input("What string would you like to replace? (case sensitive)")
        new_string = input("What string would you like to replace it with?")
        sentence = sentence.replace(old_string, new_string)
    else:
        print("Invalid Option")

    print("Updated sentence:", sentence)

    again = input("Do you want to make any other changes? (y/n)")
    if again == "n": 
        print("Thank you for using the sentence manager")
        break

