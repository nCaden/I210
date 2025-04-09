# Nested list of Mario characters [name, first appearance year, main series debut, role]
mario_characters = [
    ["Mario", 1981, "Donkey Kong (1981)", "Main Character"],
    ["Luigi", 1983, "Mario Bros. (1983)", "Supporting Character"],
    ["Princess Peach", 1985, "Super Mario Bros. (1985)", "Damsel in Distress"],
    ["Yoshi", 1990, "Super Mario World (1990)", "Riding Character"],
    ["Bowser", 1985, "Super Mario Bros. (1985)", "Main Antagonist"],
    ["Toad", 1985, "Super Mario Bros. (1985)", "Supporting Character"],
    ["Princess Daisy", 1989, "Super Mario Land (1989)", "Main Character"],
    ["Wario", 1992, "Super Mario Land 2: 6 Golden Coins (1992)", "Antagonist/Playable Character"],
    ["Waluigi", 2000, "Mario Tennis (2000)", "Supporting Character/Playable Character"]
]

def selection_sort(mario_list, index):
    for i in range(len(mario_list)):
        smallest_index = i
        for j in range (i + 1, len(mario_list)):
            if mario_list[j][index] < mario_list[smallest_index][index]:
                smallest_index = j
        mario_list[i], mario_list[smallest_index] = mario_list[smallest_index], mario_list[i]
    return mario_list
    

def insertion_sort(mario_list, index):
    for i in range(1, len(mario_list)):
        key_item = mario_list[i]
        j = i - 1
        while j >= 0 and mario_list[j][index] > key_item[index]:
            mario_list[j + 1] = mario_list[j]
            j -= 1
        mario_list[j + 1] = key_item
    return mario_list
    

print("Unsorted")
print(mario_characters)

print("Mario characters sorted by name using selection sort:")
print(selection_sort(mario_characters, 0))

print("\nMario characters sorted by first appearance year using insertion sort:")
print(insertion_sort(mario_characters, 1))
