import random
def create_party_tables():
    
# List of 60 people's names
    people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivy", "Jack",
    "Kate", "Liam", "Mia", "Noah", "Olivia", "Pam", "Quinn", "Ryan", "Sara", "Tom",
    "Uma", "Vera", "Will", "Xander", "Yara", "Zack", "Amber", "Ben", "Cathy", "Dylan",
    "Emily", "Finn", "Gina", "Henry", "Iris", "Jake", "Kara", "Luke", "Molly", "Nate",
    "Owen", "Penny", "Quincy", "Rachel", "Sam", "Tina", "Vincent", "Wendy", "Xavier",
    "Yvonne", "Zoe", "Adam", "Beth", "Carl", "Daisy", "Eric", "Fiona", "Greg", "Heidi",
    "Ian", "Jill", "Kyle", "Laura", "Mark", "Nina", "Oscar", "Patty", "Rob", "Stella"]

# Initialize a list of tables
    tables = []
    index = 0
    for i in range(6):
        table = []
        for j in range(10):
            table.append(people[index])
            index += 1
        tables.append(table)
    return tables

party_tables = create_party_tables()
print(party_tables)