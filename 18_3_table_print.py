# 18.3 Table print
# table_print takes a nested list, header row, and column width
# Prints out a double column table







# main
labels = ["Name", "Age"]
people = [("Sam", 20), ("Juniper", 18), ("Adam", 22), ("Susan", 19), ("Daniel", 21)]

labels2 = ["Capital", "State"]
states = [("Atlanta", "GA"), ("Boston", "MA"), ("Columbus", "OH"), ("Austin", "TX"), ("Boise", "ID")]

table_print(labels, people)
table_print(labels2, states, 15)

