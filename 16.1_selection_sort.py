numbers = [18, 3, 9, 6, 12]

for start_index in range(len(numbers) - 1):

    smallest_index = start_index
    for index in range(start_index + 1, len(numbers)):
        if numbers[smallest_index] > numbers[index]:
            smallest_index = index

    temp = numbers[start_index]
    numbers[start_index] = numbers[smallest_index]
    numbers[smallest_index] = temp

print(numbers)

#1 so we can start at what we think is the lowest value
#2 numbers[smallest_index], numbers[start_index] = numbers[smallest_index]
#3 so that we don't loop the start_index twice
#4 because the index number will change while it is being sorted
#5 change which position it is sorted by