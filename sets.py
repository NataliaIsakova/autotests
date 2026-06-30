def get_unique_elements(lst):
    return set(lst)

def is_unique_list(lst):
    return len(set(lst)) == len(lst)



def get_unique_vowels(s):
    vowels = {"a", "e", "i", "o", "u"}
    result = set()

    for letter in s.lower():
        if letter in vowels:
            result.add(letter)

    return result

print(get_unique_vowels("Hello World"))
