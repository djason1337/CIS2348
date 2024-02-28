# Dominic Jason 2203959

import csv

file1 = input()

with open(file1, 'r') as file:
    file = csv.reader(file)
    for lines in file:
        list1 = lines

nodupe = []

for word in list1:
    if word not in nodupe:
        nodupe.append(word)

for word in nodupe:
    count = list1.count(word)
    print(word, count)
