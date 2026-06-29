def remove_duplicates(lst):
    return list(set(lst))

def generate_squares(n):
    numbers = [x**2 for x in range(1, n + 1)]

    return numbers

def merge_lists(list1, list2):
    new_list = list2+list1

    return list(set(new_list))

def is_sorted(lst):
    if lst == sorted(lst):
        return True
    else: return False

def merge_lists2(list1, list2):
    return [list1[i] + list2[i] for i in range(len(list1))]

