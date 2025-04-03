import random

# List of 60 people's names
people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivy", "Jack",
    "Kate", "Liam", "Mia", "Noah", "Olivia", "Pam", "Quinn", "Ryan", "Sara", "Tom",
    "Uma", "Vera", "Will", "Xander", "Yara", "Zack", "Amber", "Ben", "Cathy", "Dylan",
    "Emily", "Finn", "Gina", "Henry", "Iris", "Jake", "Kara", "Luke", "Molly", "Nate",
    "Owen", "Penny", "Quincy", "Rachel", "Sam", "Tina", "Vincent", "Wendy", "Xavier",
    "Yvonne", "Zoe", "Adam", "Beth", "Carl", "Daisy", "Eric", "Fiona", "Greg", "Heidi",
    "Ian", "Jill", "Kyle", "Laura", "Mark", "Nina", "Oscar", "Patty", "Rob", "Stella"]

def create_tables(people):
    # Initialize a list of tables
    tables = []

    index = 0
    # Assign guests to tables
    for i in range(6):
        table = []
        for j in range(10):
            #Another solution, without using index = 0 and index += 1
            #person_index = i * 10 + j
            #table.append(people[index])
            table.append(people[index])
            index += 1
        tables.append(table)

    return tables

def remove_person(tables, person):
    for table in tables:
        if person in table:
            table.remove(person)
    return tables
print("Creating Party Tables")
tables = create_tables(people)
print(tables)

#14.2
#ask user who can't make it to the party
person = input("Who can't make it to the party?")
while person:
    #call remove person
    remove_person(tables, person)
    print("Removed", person)
    
    #ask again until empty input
    person = input("Who can't make it to the party?\nEnter empty input if no more")
removed = remove_person
print(removed(tables, person))




