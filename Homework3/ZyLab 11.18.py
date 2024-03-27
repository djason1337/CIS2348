# Dominic Jason 2203959

user_input = input()
user_input_split = user_input.split()
sorted_list = []

for num in user_input_split:
    if int(num) >= 0:
        sorted_list.append(int(num))

sorted_list.sort()


def list_print(list1):
    for number in list1:
        print(number, end=' ')


list_print(sorted_list)
