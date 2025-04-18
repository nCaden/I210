def read_file(file_name):
    if not file_name.endswith('.txt'): #makes sure that .txt is included in the input regardless if the user includes it or not
        file_name += '.txt'
    try:
        with open(file_name, 'r') as file: #attempts to open the file given by the user and will open if the there is a file in the directory that matches the input
            contents = file.read()
        return contents
    except FileNotFoundError: #if the FileNotFoundError is produced by giving an invalid file name the function will print that the file cannot be found
        print("File not found")
    # open and read the file, and return the text

def get_words(text):
    punctuation = "!#$%&\\()*+,-./:;<=>?@[]^_`{|}~" + '\n'
    # split the text into words
        # create a list to store the cleaned words
    # for each word in the text that was split into words, 
        # create a blank string called "clean_word"
        # loop over each character of the original word
            # if that character is not contained in the "puntuation" list defined above, 
                # add it to clean_word
        # append the lower cases version of the clean word to the list of cleaned words
    # return the list of cleaned words
    words = text.split()
    clean_words = []
    for word in words:   #this loop finds all the words and makes the lowerclass while making sure to remove punctuation marks based on the punctuation variable
        clean_word = ""
        for char in word:
            if char not in punctuation:
                clean_word += char
        clean_words.append(clean_word.lower()) #appends all of these words to the list
    return clean_words

def count_words(words):
    word_count = {} # Create a dictionary to hold word frequencies
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # Iterate over the words to update the dictionary 
    # return the dictionary
    return word_count

def display_results(word_counts):
    word_list = list(word_counts.items()) #changes dictionary into list
    for i in range(len(word_list)): #using selection sort the frequencies are compared and then the values are swapped depending on which frequency is bigger/smaller 
        max_index = i
        for j in range(i + 1, len(word_list)):
            if word_list[j][1] > word_list[max_index][1]:  # Compare frequencies
                max_index = j
        word_list[i], word_list[max_index] = word_list[max_index], word_list[i] #swap indexes
    # create a list from the keys and values in your word_counts dictionary. 
    # sort the list by value, in descending order. You can use insertion sort, selection sort, key sorting, or lambda sorting
    # print out the top 20 words and the number of times they were used
    print(f"{'Word':<15}{'Frequency':<10}")
    print("-" * 25)
    for word, frequency in word_list[:20]: #selects the top 20 most frequent words
        print(f"{word:<15}{frequency:<10}") #prints out the 20 most frequent words with formatted spaces to the left of the words to form columns


#main

# Ask the user for the file they wish to open
file_name = input("Which file would you like to open: ")

    
# Read the file & print the returned string
print("--------Stage 1--------")   
text = read_file(file_name)
print(text)


# Split into individual words
print("--------Stage 2--------")  
words = get_words(text)
print(words)


# Count the words
print("--------Stage 3--------")  
word_count = count_words(words)
print(word_count)


# Display the results
print("--------Stage 4--------")  
words = display_results(word_count)   

