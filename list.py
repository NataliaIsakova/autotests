def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result

def generate_squares(n):
    numbers = [x**2 for x in range(1, n + 1)]

    return numbers

def merge_lists(list1, list2):
    new_list = list2+list1

    return list(set(new_list))

def is_sorted(lst):
    return lst == sorted(lst)

def merge_lists2(list1, list2):
    if len(list1) != len(list2):
        return False

    result = []

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result

