def sum_numbers(n):
    total = 0
    for number in range(1, n + 1):
        total += number
    return total

def find_min(numbers):
    minim = numbers[0]
    for number in numbers:
        if number < minim:
            minim = number
    return minim

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count

def print_diamond(rows):
    for i in range(1, rows + 1):
        print("*" * i)
    for i in range(rows - 1, 0, -1):
        print("*" * i)

def countdown():
    for i in range(10, 0, -1):
        print(i)
        print("Старт!")

def countdown2():
    num = 10
    while num >=1:
        print(num)
        num -= 1
        print("Старт!")