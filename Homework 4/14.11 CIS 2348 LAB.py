# Dominic Jason 2203959

def selection_sort_descend_trace(list):
    n = len(list)
    for i in range(n-1):
        max_value = i
        for x in range(i+1, n):
            if list[x] > list[max_value]:
                max_value = x
        list[i], list[max_value] = list[max_value], list[i]
        for num in list:
            print(num, end=" ")
        print()

if __name__ == "__main__":
    list = [int(j) for j in input().split()]
    selection_sort_descend_trace(list)