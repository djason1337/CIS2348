# Dominic Jason 2203959

user_input = input()

lines = user_input.split()

list1 = []

for line in lines:
    list1.append(line)

for word in list1:
    count = list1.count(word)
    print(word, count)
