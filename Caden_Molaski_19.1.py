import csv
def table_print(data):

    print(f"{'EPISODE':<10} {'TITLE'}")
    print("-" * 30)
    for episode, title in data:
        print(f"{episode:<10} {title}")

table_data = []

with open('codelike_bob_ross.csv', 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        episode = row['EPISODE']
        title = row['TITLE']
        season = episode[2] 

        if (season == '1' and title.startswith('A')) or (season == '3' and title.startswith('B')):
            table_data.append((episode, title))

table_print(table_data)