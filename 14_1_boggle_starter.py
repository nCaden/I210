import random
import string

ALL_LETTERS = string.ascii_uppercase
boggle_board = []
#14.1
def generate_random_boggle(height, width):
    for i in range(height):
        letters = []
        for i in range(width):
            letter = random.choice(ALL_LETTERS)
            letters.append(letter)
        boggle_board.append(letters)
    return boggle_board

#14.2
def print_boggle(boggle):
    for i in range(len(boggle)):
        for letter in range(len(boggle[i])):
            print(boggle[i][letter], end = " ")
        print()
    

new_boggle_board = generate_random_boggle(4,4)
(print_boggle(new_boggle_board))