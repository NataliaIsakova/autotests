a = int(input('Длина:'))
b = int(input('Ширина:'))
sq = a * b
def rectangle_area(a, b):
    return print(f"Площадь прямоугольника с длиной {a} и шириной {b} равна {sq}.")

rectangle_area(a,b)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return print(f'В {seconds} секундах содержится {hours} час(ов) и {minutes} минут(ы).')

def power_of(number, exponent=2):
    result = number ** exponent
    return f'Число {number} в степени {exponent} равно {result}.'

def count_items(*args):
    return len(args)