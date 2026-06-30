from dz import result


def char_frequency(s):
    result = {}

    for char in s:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    return result


def merge_dicts(dict1, dict2):
   result = dict1.copy()
   for key, value in dict2.items():
        if key in result:
            result[key]+=value
        else:
            result[key] = value

   return result

def dict_to_lists(my_dict):
    keys = list(my_dict.keys())
    values = list(my_dict.values())

    return keys, values


def group_by_first_letter(strings):
    result = {}

    for word in strings:
        first_letter = word[0]

        if first_letter not in result:
            result[first_letter] = []

        result[first_letter].append(word)

    return result


def extract_subdict(my_dict, keys):
    result = {}

    for key in keys:
        if key in my_dict:
            result[key] = my_dict[key]

    return result


