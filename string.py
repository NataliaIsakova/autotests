def is_anagram(s1, s2):
    return  sorted(s1.lower()) == sorted(s2.lower())


def is_palindrome(s):
    s = s.lower()
    clean = ""

    for letter in s:
        if letter.isalnum():
            clean += letter

    return clean == clean[::-1]


def longest_word(s):
    words = s.split()
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

def format_phone_number(digits):
    return f'({digits[0:3]}) {digits[3:6]}-{digits[6:]}'

def remove_duplicates(s):
    result = ""

    for letter in s:
        if letter not in result:
            result += letter

    return result

def is_unique(s):
    is_seen = ""

    for letter in s:
        if letter in is_seen:
            return False
        is_seen += letter

    return True