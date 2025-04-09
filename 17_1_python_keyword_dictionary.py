# 17.1 Python keyword dictionary
# Write a program that takes in a Python keyword and provides a definition

# Python keywords and definitions to add to your dictionary
# "while": "statement that repeats as long as an expression is true"
# "for": "statement that iterates through elements in a sequence"

# use when adding in a new keyword
def valid_keyword(word):
    all_keywords = ["False", "await", "else", "import", "pass", "None", "break", "True", "class", "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "from", "nonlocal", "while", "assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield"]
    return word in all_keywords

# globals
keywords = {
    "False": "boolean object",
    "True": "boolean object",
    "if": "conditional - helps make decisions - see elif, else",
    "else": "conditional - helps make decisions - see if, elif",
    "elif": "conditional - helps make decisions - see if, else",
    "and": "boolean operator - helps with program logic",
    "not": "boolean operator - helps with program logic",
    "or": "boolean operator - helps with program logic",
    "return": "returns values from a function definition",
    "def": "defines a function",
    "in": "tests for membership",
    "import": "connects modules together"
}

# main

# ask the user for a keyword, or 'keys' for all choices
# while there is possible word for the dictionary
# ask the user for a keyword and provide a definition
# if they type in 'keys', print out all of the options
# if they type in a word not in the dictionary,
#   print a message that the word wasn't found
#   check that the word is a Python keyword (use the function we provide!)
#   if it is, then prompt for a definition and add it to dictionary
while True:
    user_keyword = input("Enter a keyword or 'keys' for all choices: ")
    if user_keyword == '':
        break
    elif user_keyword == 'keys':
        for key in keywords.keys():
            print(key, end="\t")
        print()
    elif user_keyword in keywords:
        print(keywords[user_keyword])
    elif user_keyword not in keywords:
        if valid_keyword(user_keyword):
            add_definition = input("add a definition: ")
            if add_definition != "":
                keywords[user_keyword] = add_definition
    