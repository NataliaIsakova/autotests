def remove_duplicates(lst):
    result = []
    is_set = set()

    for item in lst:
        if item not in is_set:
            is_set.add(item)
            result.append(item)

    return result

def generate_squares(n):
    numbers = [x**2 for x in range(1, n + 1)]

    return numbers

def merge_lists(list1, list2):
    new_list = list2+list1

    return list(set(new_list))

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True

def merge_lists2(list1, list2):
    if len(list1) != len(list2):
        return False

    result = []

    for first, second in zip(list1, list2):
        result.append(first + second)

    return result

