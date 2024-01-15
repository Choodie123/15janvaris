import csv

with open('text.txt', 'r', encoding='utf8') as file:
    data = csv.reader(file)
    kolonna = 1 # prima kolonna ir ar index 0
    for row in data:
        res = row[0].split()
        print(res[kolonna])
