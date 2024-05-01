# Dominic Jason 2203959

# global variable
num_calls = 0

# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary


def partition(user_ids, i, k):
    index_pivot = (i+k) // 2
    value_pivot = user_ids[index_pivot]

    user_ids[index_pivot], user_ids[k] = user_ids[k], user_ids[index_pivot]
    high = k - 1
    low = i

    while low <= high:
        while user_ids[low] < value_pivot:
            low += 1

        while user_ids[high] > value_pivot:
            high -= 1

        if low < high:
            high -= 1
            low += 1
            user_ids[low], user_ids[high] = user_ids[high], user_ids[low]

    user_ids[k], user_ids[low] = user_ids[low], user_ids[k]
    return low


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quicksort() is called


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if i < k:

        index_pivot = partition(user_ids, i, k)

        quicksort(user_ids, i, index_pivot - 1)

        quicksort(user_ids, index_pivot + 1, k)


# main flow


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # print number of calls to quicksort
    print(num_calls)

    # print sorted user ids
    for user_id in user_ids:
        print(user_id)
